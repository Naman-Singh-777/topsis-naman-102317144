\# TOPSIS Implementation



\*\*Name:\*\* Naman Singh  

\*\*Roll Number:\*\* 102317144  

\*\*Course:\*\* UCS654 - Predictive Data Analytics



\## About



This package implements TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) for multi-criteria decision making.



\## Installation

```bash

pip install Topsis-Naman-102317144

```



\## Usage



\### Command Line (Part I)

```bash

python topsis.py input.csv "1,1,1,2" "+,+,-,+" output.csv

```



\### As Package (Part II)

```bash

topsis input.csv "1,1,1,2" "+,+,-,+" output.csv

```



\### Web Interface (Part III)

```bash

python app.py

```

Then visit http://localhost:5000



\## Input Format



CSV file with:

\- First column: Alternative names

\- Other columns: Numeric criteria values



Example:

```csv

Fund,Return,Risk,Expense

A,12.5,0.8,1.2

B,10.2,0.6,0.9

```



\## Parameters



\*\*Weights:\*\* Comma-separated numbers representing importance of each criterion  

Example: "1,2,1" means second criterion has double weight



\*\*Impacts:\*\* + for benefit (higher is better), - for cost (lower is better)  

Example: "+,-,+" means first and third are benefits, second is cost



\## Requirements



\- Python 3.6+

\- pandas

\- numpy

\- Flask (for web service)



\## License



MIT License - See LICENSE.txt for details



\## Author



Naman Singh (102317144)

