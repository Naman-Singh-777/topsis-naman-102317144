import pandas as pd
import numpy as np
import sys
import os

def normalize_matrix(df):
    """Normalize the decision matrix using root of sum of squares"""
    normalized = df.copy()
    for col in df.columns:
        sum_sq = np.sqrt((df[col] ** 2).sum())
        normalized[col] = df[col] / sum_sq
    return normalized

def calc_weighted_matrix(normalized_df, weights):
    """Apply weights to normalized matrix"""
    weighted = normalized_df.copy()
    for i, col in enumerate(normalized_df.columns):
        weighted[col] = normalized_df[col] * weights[i]
    return weighted

def get_ideal_solutions(weighted_df, impacts):
    """Calculate ideal best and worst solutions"""
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
    """Calculate euclidean distance from ideal solution"""
    distances = []
    for idx in range(len(weighted_df)):
        row_vals = weighted_df.iloc[idx].values
        dist = np.sqrt(sum((row_vals[i] - ideal_solution[i]) ** 2 
                          for i in range(len(ideal_solution))))
        distances.append(dist)
    return distances

def topsis_score_calc(dist_best, dist_worst):
    """Calculate final TOPSIS score"""
    scores = []
    for i in range(len(dist_best)):
        score = dist_worst[i] / (dist_best[i] + dist_worst[i])
        scores.append(score)
    return scores

def validate_inputs(input_file, weights, impacts, output_file):
    """Validate all inputs before processing"""
    
    # Check if input file exists
    if not os.path.isfile(input_file):
        print(f"Error: File '{input_file}' not found!")
        return False
    
    # Check file extension
    if not (input_file.endswith('.csv') or input_file.endswith('.xlsx')):
        print("Error: Input file must be CSV or Excel format")
        return False
    
    # Read the file
    try:
        if input_file.endswith('.csv'):
            df = pd.read_csv(input_file)
        else:
            df = pd.read_excel(input_file)
    except Exception as e:
        print(f"Error reading file: {e}")
        return False
    
    # Check minimum columns
    if len(df.columns) < 3:
        print("Error: Input file must have at least 3 columns")
        return False
    
    # Check numeric values in columns 2 onwards
    numeric_cols = df.columns[1:]
    for col in numeric_cols:
        if not pd.api.types.is_numeric_dtype(df[col]):
            print(f"Error: Column '{col}' contains non-numeric values")
            return False
    
    # Parse weights and impacts
    try:
        weight_list = [float(w.strip()) for w in weights.split(',')]
        impact_list = [i.strip() for i in impacts.split(',')]
    except:
        print("Error: Invalid format for weights or impacts")
        return False
    
    # Check counts match
    num_criteria = len(numeric_cols)
    if len(weight_list) != num_criteria:
        print(f"Error: Number of weights ({len(weight_list)}) doesn't match number of columns ({num_criteria})")
        return False
    
    if len(impact_list) != num_criteria:
        print(f"Error: Number of impacts ({len(impact_list)}) doesn't match number of columns ({num_criteria})")
        return False
    
    # Validate impacts are + or -
    for imp in impact_list:
        if imp not in ['+', '-']:
            print(f"Error: Impact must be '+' or '-', got '{imp}'")
            return False
    
    return True

def run_topsis(input_file, weights, impacts, output_file):
    """Main TOPSIS calculation function"""
    
    # Read input file
    if input_file.endswith('.csv'):
        df = pd.read_csv(input_file)
    else:
        df = pd.read_excel(input_file)
    
    # Parse weights and impacts
    weight_list = [float(w.strip()) for w in weights.split(',')]
    impact_list = [i.strip() for i in impacts.split(',')]
    
    # Extract data
    fund_names = df.iloc[:, 0]
    data_matrix = df.iloc[:, 1:]
    
    # Step 1: Normalize
    norm_matrix = normalize_matrix(data_matrix)
    
    # Step 2: Apply weights
    weighted_matrix = calc_weighted_matrix(norm_matrix, weight_list)
    
    # Step 3: Get ideal solutions
    ideal_best, ideal_worst = get_ideal_solutions(weighted_matrix, impact_list)
    
    # Step 4: Calculate distances
    dist_from_best = calc_euclidean_dist(weighted_matrix, ideal_best)
    dist_from_worst = calc_euclidean_dist(weighted_matrix, ideal_worst)
    
    # Step 5: Calculate TOPSIS scores
    topsis_scores = topsis_score_calc(dist_from_best, dist_from_worst)
    
    # Step 6: Rank the alternatives
    result_df = df.copy()
    result_df['Topsis Score'] = topsis_scores
    result_df['Rank'] = pd.Series(topsis_scores).rank(ascending=False).astype(int)
    
    # Save output
    result_df.to_csv(output_file, index=False)
    print(f"Results saved to {output_file}")
    
    return result_df

def main():
    # Check number of arguments
    if len(sys.argv) != 5:
        print("Error: Incorrect number of parameters")
        print("Usage: python topsis.py <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        print("Example: python topsis.py data.csv \"1,1,1,2\" \"+,+,-,+\" result.csv")
        sys.exit(1)
    
    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    output_file = sys.argv[4]
    
    # Validate inputs
    if not validate_inputs(input_file, weights, impacts, output_file):
        sys.exit(1)
    
    # Run TOPSIS
    try:
        run_topsis(input_file, weights, impacts, output_file)
    except Exception as e:
        print(f"Error during TOPSIS calculation: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
