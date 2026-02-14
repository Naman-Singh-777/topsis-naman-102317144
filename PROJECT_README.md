# TOPSIS Implementation - Complete Package

A comprehensive Python implementation of TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) for multi-criteria decision making.

## 🎯 Features

- ✅ **Command-line tool** for quick TOPSIS analysis
- ✅ **PyPI package** for easy installation and integration
- ✅ **Web service** with email delivery of results
- ✅ **Comprehensive error handling** and validation
- ✅ **Support for CSV and Excel** input files
- ✅ **Easy to use** with minimal setup

## 📦 Installation

### Quick Install

```bash
pip install Topsis-Naman-102317144
```

### From Source

```bash
git clone https://github.com/naman-singh/topsis-package
cd topsis-package
pip install -r requirements.txt
```

## 🚀 Quick Start

### Command Line

```bash
topsis data.csv "1,1,1,1" "+,+,-,+" result.csv
```

### Python Code

```python
from Topsis_Naman_102317144 import run_topsis

run_topsis('data.csv', '1,1,1,1', '+,+,-,+', 'result.csv')
```

### Web Interface

```bash
python app.py
# Open http://localhost:5000 in browser
```

## 📋 What is TOPSIS?

TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) is a multi-criteria decision analysis method. It helps you choose the best alternative from a set of options by:

1. Normalizing decision matrix
2. Applying weights to criteria
3. Finding ideal best and worst solutions
4. Calculating relative closeness to ideal best
5. Ranking alternatives

## 📊 Input Format

Your input file should look like this:

```csv
Fund Name,P1,P2,P3,P4,P5
M1,0.84,0.71,6.7,42.1,12.59
M2,0.91,0.83,7.0,31.7,10.11
M3,0.79,0.62,4.8,46.7,13.23
```

- **First column**: Alternative names
- **Other columns**: Numeric criteria values

## 🔧 Usage Examples

### Example 1: Simple Analysis

```bash
topsis input.csv "1,1,1,2" "+,+,-,+" output.csv
```

This analyzes a file with 4 criteria where:
- First 3 have equal weight (1)
- Last has double weight (2)
- First 2 are benefits (+)
- Third is cost (-)
- Fourth is benefit (+)

### Example 2: Python Integration

```python
import pandas as pd
from Topsis_Naman_102317144 import run_topsis

# Run TOPSIS
result = run_topsis(
    input_file='funds.csv',
    weights='2,1,1,1',
    impacts='+,-,-,+',
    output_file='ranked_funds.csv'
)

# Get top 3
top_3 = result.nsmallest(3, 'Rank')
print(top_3)
```

## 🌐 Web Service

Start the web server:

```bash
python app.py
```

Features:
- Upload CSV/Excel files
- Enter weights and impacts
- Get results via email
- Clean, modern UI

## ⚙️ Parameters

### Weights
Comma-separated numbers representing importance of each criterion.
- Example: `"1,2,1,1"` - Second criterion has double weight

### Impacts
Comma-separated + or - for each criterion.
- `+` = Higher is better (benefit criterion)
- `-` = Lower is better (cost criterion)
- Example: `"+,+,-,+"` - Third is cost, others are benefits

## 🛡️ Error Handling

The package validates:
- File existence and format
- Correct number of parameters
- Numeric values in criteria columns
- Matching counts of weights, impacts, and criteria
- Valid impact values (+ or -)
- Email format (for web service)

## 📖 Documentation

- [User Manual](USER_MANUAL.md) - Detailed usage guide
- [API Documentation](docs/API.md) - For developers
- [Examples](examples/) - Sample datasets and use cases

## 🧪 Testing

Test with sample data:

```bash
# Using included sample data
topsis data.csv "1,1,1,1,1" "+,+,-,+,+" result.csv

# View results
cat result.csv
```

## 📁 Project Structure

```
topsis-package/
├── Topsis-Naman-102317144/     # Main package
│   ├── __init__.py
│   ├── __main__.py
│   └── topsis_calc.py
├── templates/                   # Web UI templates
│   └── index.html
├── topsis.py                    # Standalone script
├── app.py                       # Web service
├── setup.py                     # Package setup
├── requirements.txt
├── README.md
├── USER_MANUAL.md
└── LICENSE.txt
```

## 🔍 How It Works

```
Input Data
    ↓
Normalize Matrix (using root of sum of squares)
    ↓
Apply Weights
    ↓
Find Ideal Best & Ideal Worst Solutions
    ↓
Calculate Euclidean Distances
    ↓
Calculate TOPSIS Score = D- / (D+ + D-)
    ↓
Rank Alternatives (higher score = better)
    ↓
Output Results
```

## 💡 Use Cases

- **Investment Analysis**: Compare mutual funds, stocks
- **Product Selection**: Choose best laptop, phone, etc.
- **Vendor Evaluation**: Select best supplier
- **Project Prioritization**: Rank project proposals
- **Location Selection**: Choose optimal site
- **HR Decisions**: Candidate evaluation

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📝 License

MIT License - see [LICENSE.txt](LICENSE.txt)

## 👨‍💻 Author

**Naman Singh**  
Roll Number: 102317144  
Email: nsingh1_be23@thapar.edu

## 🙏 Acknowledgments

- TOPSIS method by Hwang and Yoon (1981)
- Flask framework for web service
- Pandas and NumPy for data processing

## 📞 Support

For issues or questions:
- Open an issue on GitHub
- Check the [User Manual](USER_MANUAL.md)
- Email: nsingh1_be23@thapar.edu

## 🔄 Version

Current version: **1.0.3**

## 📊 Performance

- Handles datasets with 1000+ alternatives
- Processes typical dataset in < 1 second
- Minimal memory footprint

## 🎓 Educational Use

This package was developed as part of a Data Analytics course assignment. Feel free to use it for:
- Learning MCDM techniques
- Teaching decision analysis
- Academic projects
- Research work

---

**Star ⭐ this repository if you find it helpful!**
