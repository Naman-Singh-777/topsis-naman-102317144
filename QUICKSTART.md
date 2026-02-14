# Quick Start Guide - TOPSIS Package

## 5-Minute Setup

### Option 1: Use Command-Line Script (Fastest)

```bash
# 1. Download the script
wget https://raw.githubusercontent.com/your-repo/topsis.py

# 2. Prepare your data (CSV format)
# First column: Names, Other columns: Numeric values

# 3. Run TOPSIS
python topsis.py yourdata.csv "1,1,1,2" "+,+,-,+" result.csv

# Done! Check result.csv
```

### Option 2: Install from PyPI

```bash
# 1. Install
pip install Topsis-Naman-102317144

# 2. Use anywhere
topsis data.csv "1,1,1,1" "+,+,-,+" output.csv

# That's it!
```

### Option 3: Web Interface

```bash
# 1. Clone repo
git clone https://github.com/your-repo/topsis-package
cd topsis-package

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start server
python app.py

# 4. Open browser
# Go to http://localhost:5000
# Upload file, enter weights/impacts, get results by email
```

---

## Example Data Format

Create a file called `mydata.csv`:

```csv
Option,Cost,Quality,Speed,Reliability
A,100,8.5,75,90
B,150,9.2,85,95
C,120,8.0,80,88
D,200,9.5,90,98
```

Run TOPSIS:

```bash
topsis mydata.csv "1,2,2,1" "-,+,+,+" result.csv
```

Output will have:
- All original columns
- Topsis Score
- Rank (1 = best)

---

## Parameters Explained

**Weights:** How important each criterion is
- Example: `"1,2,2,1"` means criteria 2 and 3 are twice as important

**Impacts:** Is higher better or worse?
- `+` = Higher is better (quality, speed)
- `-` = Lower is better (cost, time)
- Example: `"-,+,+,+"` means first is cost (lower better), rest are benefits

---

## Common Commands

```bash
# Basic usage
topsis input.csv "1,1,1,1" "+,+,+,+" output.csv

# Different weights
topsis input.csv "2,1,1,3" "+,+,-,+" output.csv

# All cost criteria
topsis input.csv "1,1,1" "-,-,-" output.csv

# All benefit criteria  
topsis input.csv "1,1,1" "+,+,+" output.csv
```

---

## Python Usage

```python
from Topsis_Naman_102317144 import run_topsis

# Simple
run_topsis('data.csv', '1,1,1,1', '+,+,-,+', 'result.csv')

# With pandas
import pandas as pd
result = run_topsis('data.csv', '1,1,1,1', '+,+,-,+', 'result.csv')
print(result.head())

# Get top 3
top_3 = result.nsmallest(3, 'Rank')
print(top_3)
```

---

## Troubleshooting

**Problem:** "Module not found"
```bash
pip install Topsis-Naman-102317144
```

**Problem:** "File not found"
```bash
# Use full path
topsis /path/to/data.csv "1,1" "+,+" result.csv
```

**Problem:** "Invalid weights format"
```bash
# Use commas, no spaces
# ✓ Correct: "1,2,1,1"
# ✗ Wrong: "1, 2, 1, 1"
```

**Problem:** "Counts don't match"
```bash
# If you have 4 criteria columns:
# Need 4 weights and 4 impacts
topsis data.csv "1,1,1,1" "+,+,-,+" result.csv
```

---

## What You Get

Input:
```csv
Fund,Return,Risk,Expense
A,12.5,0.8,1.2
B,10.2,0.6,0.9
C,15.1,1.1,1.5
```

Output:
```csv
Fund,Return,Risk,Expense,Topsis Score,Rank
A,12.5,0.8,1.2,0.523,2
B,10.2,0.6,0.9,0.687,1
C,15.1,1.1,1.5,0.412,3
```

Higher Topsis Score = Better option
Rank 1 = Best choice

---

## Full Documentation

For detailed guide, see:
- [User Manual](USER_MANUAL.md) - Complete usage guide
- [Project README](PROJECT_README.md) - Full documentation
- [PyPI Upload Guide](PYPI_UPLOAD_GUIDE.md) - For package authors

---

## Need Help?

1. Check error message
2. Verify input format
3. Read [USER_MANUAL.md](USER_MANUAL.md)
4. Open GitHub issue

---

**You're all set! Start analyzing with TOPSIS! 🚀**
