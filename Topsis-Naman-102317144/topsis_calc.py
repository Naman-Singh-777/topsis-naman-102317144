import pandas as pd
import numpy as np
import os

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
    """Get ideal best and worst"""
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
    """Calculate euclidean distance"""
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

def validate_inputs(input_file, weights, impacts, output_file):
    """Validate inputs"""
    
    if not os.path.isfile(input_file):
        raise FileNotFoundError(f"File '{input_file}' not found!")
    
    if not (input_file.endswith('.csv') or input_file.endswith('.xlsx')):
        raise ValueError("Input file must be CSV or Excel format")
    
    try:
        if input_file.endswith('.csv'):
            df = pd.read_csv(input_file)
        else:
            df = pd.read_excel(input_file)
    except Exception as e:
        raise Exception(f"Error reading file: {e}")
    
    if len(df.columns) < 3:
        raise ValueError("Input file must have at least 3 columns")
    
    numeric_cols = df.columns[1:]
    for col in numeric_cols:
        if not pd.api.types.is_numeric_dtype(df[col]):
            raise ValueError(f"Column '{col}' contains non-numeric values")
    
    try:
        weight_list = [float(w.strip()) for w in weights.split(',')]
        impact_list = [i.strip() for i in impacts.split(',')]
    except:
        raise ValueError("Invalid format for weights or impacts")
    
    num_criteria = len(numeric_cols)
    if len(weight_list) != num_criteria:
        raise ValueError(f"Number of weights doesn't match number of columns")
    
    if len(impact_list) != num_criteria:
        raise ValueError(f"Number of impacts doesn't match number of columns")
    
    for imp in impact_list:
        if imp not in ['+', '-']:
            raise ValueError(f"Impact must be '+' or '-', got '{imp}'")
    
    return True

def run_topsis(input_file, weights, impacts, output_file):
    """Main TOPSIS function"""
    
    # Validate first
    validate_inputs(input_file, weights, impacts, output_file)
    
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
    
    result_df.to_csv(output_file, index=False)
    
    return result_df
