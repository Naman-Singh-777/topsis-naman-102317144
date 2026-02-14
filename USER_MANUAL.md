# TOPSIS Package - User Manual

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Part I - Command Line Usage](#part-i---command-line-usage)
4. [Part II - PyPI Package](#part-ii---pypi-package)
5. [Part III - Web Service](#part-iii---web-service)
6. [Input File Format](#input-file-format)
7. [Examples](#examples)
8. [Troubleshooting](#troubleshooting)

---

## Introduction

This package implements TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution), a multi-criteria decision analysis method. TOPSIS helps you choose the best option from multiple alternatives based on several criteria.

### How TOPSIS Works

1. **Normalize** the decision matrix
2. **Weight** the normalized matrix
3. Find **ideal best** and **ideal worst** solutions
4. Calculate **distance** from each alternative to ideal solutions
5. Calculate **relative closeness** to ideal best
6. **Rank** alternatives

---

## Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package manager)

### Install from PyPI

```bash
pip install Topsis-Naman-102317144
```

### Install from Source

```bash
git clone https://github.com/naman-singh/topsis-package
cd topsis-package
pip install -r requirements.txt
python setup.py install
```

---

## Part I - Command Line Usage

### Standalone Script

If you have the `topsis.py` file:

```bash
python topsis.py <InputFile> <Weights> <Impacts> <OutputFile>
```

**Example:**
```bash
python topsis.py data.csv "1,1,1,1,1" "+,+,-,+,+" result.csv
```

### Parameters

1. **InputFile**: Path to CSV or Excel file with decision matrix
2. **Weights**: Comma-separated weights for each criterion
3. **Impacts**: Comma-separated + or - for each criterion
   - `+` = higher is better (benefit)
   - `-` = lower is better (cost)
4. **OutputFile**: Path where results will be saved

### Error Messages

The program validates:
- ✓ Correct number of parameters
- ✓ File exists
- ✓ File has minimum 3 columns
- ✓ All criteria columns are numeric
- ✓ Weights and impacts count matches criteria count
- ✓ Impacts are only + or -

---

## Part II - PyPI Package

### After Installation

Once installed via pip, you can use the `topsis` command anywhere:

```bash
topsis data.csv "1,2,1,1" "+,-,+,+" output.csv
```

### Using in Python Code

```python
from Topsis_Naman_102317144 import run_topsis

# Run TOPSIS
result = run_topsis(
    input_file='data.csv',
    weights='1,1,1,1,1',
    impacts='+,+,-,+,+',
    output_file='result.csv'
)

print(result)
```

### Update Package

To update to the latest version:

```bash
pip install --upgrade Topsis-Naman-102317144
```

---

## Part III - Web Service

### Starting the Server

```bash
python app.py
```

The server will start at `http://localhost:5000`

### Using the Web Interface

1. Open browser and go to `http://localhost:5000`
2. Fill in the form:
   - **Upload File**: Select your CSV/Excel file
   - **Weights**: Enter comma-separated weights (e.g., 1,1,1,2)
   - **Impacts**: Enter comma-separated impacts (e.g., +,+,-,+)
   - **Email**: Enter your email address
3. Click "Analyze & Send Results"
4. Check your email for results

### Email Configuration

Before using email functionality, update `app.py`:

```python
sender_email = "your_email@gmail.com"
sender_password = "your_app_password"
```

**For Gmail:**
1. Enable 2-factor authentication
2. Generate an App Password
3. Use that password in the code

---

## Input File Format

### CSV Format

```csv
Fund Name,P1,P2,P3,P4,P5
M1,0.84,0.71,6.7,42.1,12.59
M2,0.91,0.83,7.0,31.7,10.11
M3,0.79,0.62,4.8,46.7,13.23
```

### Excel Format

Same structure as CSV, just save as .xlsx

### Requirements

- First column: Names/IDs (can be text)
- Remaining columns: Numeric criteria values
- At least 3 columns total (1 name + 2 criteria minimum)
- No missing values in criteria columns

---

## Examples

### Example 1: Mutual Fund Selection

**Scenario**: Choose best mutual fund based on:
- Return (higher is better) - weight: 2
- Risk (lower is better) - weight: 1
- Expense ratio (lower is better) - weight: 1
- Fund size (higher is better) - weight: 1

**Input (funds.csv):**
```csv
Fund,Return,Risk,Expense,Size
Fund A,12.5,0.8,1.2,500
Fund B,10.2,0.6,0.9,750
Fund C,15.1,1.1,1.5,400
```

**Command:**
```bash
topsis funds.csv "2,1,1,1" "+,-,-,+" result.csv
```

**Output:** Fund B might rank highest (good return, low risk, low expense)

### Example 2: Laptop Selection

**Scenario**: Choose laptop based on:
- Performance (higher better) - weight: 3
- Price (lower better) - weight: 2
- Weight (lower better) - weight: 1
- Battery (higher better) - weight: 2

**Input (laptops.csv):**
```csv
Model,Performance,Price,Weight,Battery
Laptop X,85,60000,1.8,10
Laptop Y,92,75000,2.1,8
Laptop Z,78,55000,1.5,12
```

**Command:**
```bash
topsis laptops.csv "3,2,1,2" "+,-,-,+" laptop_result.csv
```

### Example 3: Using in Python

```python
from Topsis_Naman_102317144 import run_topsis
import pandas as pd

# Run analysis
result_df = run_topsis(
    'data.csv',
    '1,1,1,1',
    '+,+,-,+',
    'output.csv'
)

# Display top 3
top_3 = result_df.nsmallest(3, 'Rank')
print("Top 3 alternatives:")
print(top_3)
```

---

## Troubleshooting

### Common Issues

**1. "File not found" error**
- Check file path is correct
- Use absolute path if needed
- Make sure file exists

**2. "Invalid format for weights"**
- Use commas, no spaces: `1,2,1,1`
- Not: `1, 2, 1, 1` or `1 2 1 1`

**3. "Column contains non-numeric values"**
- Check all criteria columns have only numbers
- First column can be text (names)
- Remove any text from criteria columns

**4. "Number of weights doesn't match"**
- Count your criteria columns (excluding first column)
- Provide exact same number of weights and impacts
- Example: 5 criteria → 5 weights, 5 impacts

**5. "Impact must be + or -"**
- Use only `+` or `-` characters
- No spaces between them
- Correct: `+,-,+,+`
- Wrong: `+ , - , + , +`

**6. Email not sending (Web service)**
- Check email credentials in `app.py`
- Use App Password for Gmail
- Check internet connection
- Verify recipient email is correct

### Getting Help

If you encounter issues:
1. Check this manual
2. Verify input file format
3. Try example commands first
4. Check error messages carefully

---

## Technical Details

### TOPSIS Algorithm Steps (Internal)

```python
# 1. Normalize
normalized = value / sqrt(sum of squares)

# 2. Apply weights
weighted = normalized * weight

# 3. Ideal solutions
ideal_best = max/min of each column (based on impact)
ideal_worst = min/max of each column

# 4. Distance calculation
distance = sqrt(sum of squared differences)

# 5. TOPSIS score
score = distance_from_worst / (distance_from_best + distance_from_worst)

# 6. Rank
rank by score (higher is better)
```

### Dependencies

- **pandas**: Data manipulation
- **numpy**: Numerical calculations
- **Flask**: Web framework (for web service)
- **openpyxl**: Excel file support

---

## Version History

**v1.0.3** (Current)
- Full TOPSIS implementation
- Command-line interface
- PyPI package support
- Web service with email
- Comprehensive error handling

---

## License

MIT License - Free to use and modify

## Author

Naman Singh (Roll Number: 102317144)

---

**End of User Manual**
