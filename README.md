# TOPSIS Implementation in Python

A simple command-line tool and Python package for performing TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) analysis on multi-criteria decision-making problems.

## What is TOPSIS?

TOPSIS is a method used to find the best alternative from a set of options based on multiple criteria. It works by:
1. Normalizing the decision matrix
2. Applying weights to criteria
3. Finding ideal best and worst solutions
4. Calculating distances from these ideal points
5. Ranking alternatives based on relative closeness to the ideal best

## Installation

You can install this package using pip:

```bash
pip install Topsis-Naman-102317144
```

## Usage

### Command Line

After installation, you can use the `topsis` command directly from terminal:

```bash
topsis <InputDataFile> <Weights> <Impacts> <ResultFileName>
```

**Example:**
```bash
topsis data.csv "1,1,1,1,1" "+,+,-,+,+" result.csv
```

### Python Package

You can also import and use it in your Python code:

```python
from Topsis_Naman_102317144 import run_topsis

# Run TOPSIS analysis
run_topsis('data.csv', '1,1,1,1,1', '+,+,-,+,+', 'result.csv')
```

## Input File Format

The input file should be a CSV or Excel file with:
- First column: Name/ID of alternatives
- Remaining columns: Criteria values (numeric only)

**Example (data.csv):**
```
Fund Name,P1,P2,P3,P4,P5
M1,0.84,0.71,6.7,42.1,12.59
M2,0.91,0.83,7.0,31.7,10.11
M3,0.79,0.62,4.8,46.7,13.23
```

## Parameters

- **Weights**: Comma-separated numbers representing importance of each criterion
  - Example: "1,1,1,2" means 4 criteria with last one having double weight
  
- **Impacts**: Comma-separated + or - signs
  - `+` means higher value is better (benefit criteria)
  - `-` means lower value is better (cost criteria)
  - Example: "+,+,-,+,+" means 3rd criterion is cost, others are benefits

## Output

The program generates a CSV file with:
- All original columns
- **Topsis Score**: Calculated score for each alternative
- **Rank**: Ranking based on TOPSIS score (1 is best)

## Error Handling

The program checks for:
- Correct number of parameters
- File existence
- Minimum 3 columns in input
- Numeric values in criteria columns
- Matching count of weights, impacts, and criteria
- Valid impact values (+ or -)

## Example

```bash
# Install the package
pip install Topsis-Naman-102317144

# Run TOPSIS
topsis input.csv "1,2,1,1" "+,-,+,+" output.csv
```

## Requirements

- Python 3.6+
- pandas
- numpy

## License

MIT License - feel free to use this for your projects!

## Author

Naman Singh (Roll: 102317144)

## Version

1.0.3
