from flask import Flask, request, render_template, flash, redirect, url_for
import pandas as pd
import numpy as np
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import re

app = Flask(__name__)
app.secret_key = 'topsis_secret_key_12345'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['RESULT_FOLDER'] = 'results'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Create folders if they don't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['RESULT_FOLDER'], exist_ok=True)

def normalize_matrix(df):
    """Normalize decision matrix"""
    normalized = df.copy()
    for col in df.columns:
        sum_sq = np.sqrt((df[col] ** 2).sum())
        normalized[col] = df[col] / sum_sq
    return normalized

def calc_weighted_matrix(normalized_df, weights):
    """Apply weights"""
    weighted = normalized_df.copy()
    for i, col in enumerate(normalized_df.columns):
        weighted[col] = normalized_df[col] * weights[i]
    return weighted

def get_ideal_solutions(weighted_df, impacts):
    """Get ideal solutions"""
    ideal_best = []
    ideal_worst = []
    
    for i, col in enumerate(weighted_df.columns):
        if impacts[i] == '+':
            ideal_best.append(weighted_df[col].max())
            ideal_worst.append(weighted_df[col].min())
        else:
            ideal_best.append(weighted_df[col].min())
            ideal_worst.append(weighted_df[col].max())
    
    return ideal_best, ideal_worst

def calc_euclidean_dist(weighted_df, ideal_solution):
    """Calculate distance"""
    distances = []
    for idx in range(len(weighted_df)):
        row_vals = weighted_df.iloc[idx].values
        dist = np.sqrt(sum((row_vals[i] - ideal_solution[i]) ** 2 
                          for i in range(len(ideal_solution))))
        distances.append(dist)
    return distances

def topsis_score_calc(dist_best, dist_worst):
    """Calculate TOPSIS score"""
    scores = []
    for i in range(len(dist_best)):
        score = dist_worst[i] / (dist_best[i] + dist_worst[i])
        scores.append(score)
    return scores

def run_topsis_analysis(input_file, weights, impacts):
    """Run TOPSIS and return result file path"""
    
    # Read file
    if input_file.endswith('.csv'):
        df = pd.read_csv(input_file)
    else:
        df = pd.read_excel(input_file)
    
    weight_list = [float(w.strip()) for w in weights.split(',')]
    impact_list = [i.strip() for i in impacts.split(',')]
    
    fund_names = df.iloc[:, 0]
    data_matrix = df.iloc[:, 1:]
    
    # TOPSIS steps
    norm_matrix = normalize_matrix(data_matrix)
    weighted_matrix = calc_weighted_matrix(norm_matrix, weight_list)
    ideal_best, ideal_worst = get_ideal_solutions(weighted_matrix, impact_list)
    dist_from_best = calc_euclidean_dist(weighted_matrix, ideal_best)
    dist_from_worst = calc_euclidean_dist(weighted_matrix, ideal_worst)
    topsis_scores = topsis_score_calc(dist_from_best, dist_from_worst)
    
    # Create result
    result_df = df.copy()
    result_df['Topsis Score'] = topsis_scores
    result_df['Rank'] = pd.Series(topsis_scores).rank(ascending=False).astype(int)
    
    # Save result
    result_filename = f"result_{os.path.basename(input_file)}"
    result_path = os.path.join(app.config['RESULT_FOLDER'], result_filename)
    result_df.to_csv(result_path, index=False)
    
    return result_path

def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def send_email_with_attachment(recipient_email, attachment_path):
    """Send result file via email"""
    
    # Email configuration - Update with your Gmail credentials for sending emails
    sender_email = "nsingh1_be23@thapar.edu"  # Your email (use Gmail for sending)
    sender_password = "rzni rgwe ejjc elqr"  # Gmail App Password (generate from Google Account)
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = "TOPSIS Analysis Results"
    
    body = """
    Hello,
    
    Your TOPSIS analysis has been completed successfully!
    
    Please find the results attached to this email.
    
    The result file contains:
    - All your input data
    - TOPSIS Score for each alternative
    - Rank (1 being the best option)
    
    Thank you for using our TOPSIS service!
    
    Best regards,
    TOPSIS Analysis Team
    """
    
    msg.attach(MIMEText(body, 'plain'))
    
    # Attach file
    with open(attachment_path, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 
                       f"attachment; filename= {os.path.basename(attachment_path)}")
        msg.attach(part)
    
    # Send email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        return True
    except Exception as e:
        print(f"Email error: {e}")
        return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        # Get form data
        file = request.files.get('file')
        weights = request.form.get('weights')
        impacts = request.form.get('impacts')
        email = request.form.get('email')
        
        # Validate inputs
        if not file:
            flash('Please upload a file')
            return redirect(url_for('index'))
        
        if not weights or not impacts or not email:
            flash('All fields are required')
            return redirect(url_for('index'))
        
        # Validate email format
        if not validate_email(email):
            flash('Invalid email format')
            return redirect(url_for('index'))
        
        # Parse weights and impacts
        try:
            weight_list = [float(w.strip()) for w in weights.split(',')]
            impact_list = [i.strip() for i in impacts.split(',')]
        except:
            flash('Invalid format for weights or impacts')
            return redirect(url_for('index'))
        
        # Check weights and impacts count match
        if len(weight_list) != len(impact_list):
            flash('Number of weights must equal number of impacts')
            return redirect(url_for('index'))
        
        # Validate impacts
        for imp in impact_list:
            if imp not in ['+', '-']:
                flash('Impacts must be + or -')
                return redirect(url_for('index'))
        
        # Save uploaded file
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Run TOPSIS
        result_path = run_topsis_analysis(filepath, weights, impacts)
        
        # Send email
        if send_email_with_attachment(email, result_path):
            flash('Analysis completed! Results sent to your email.')
        else:
            flash('Analysis completed but email sending failed. Please check email configuration.')
        
        # Clean up uploaded file
        os.remove(filepath)
        
        return redirect(url_for('index'))
        
    except Exception as e:
        flash(f'Error: {str(e)}')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
