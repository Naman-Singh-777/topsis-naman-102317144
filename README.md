\# TOPSIS Assignment - Complete Implementation



\*\*Student Name:\*\* Naman Singh



\*\*Roll Number:\*\* 102317144



\*\*Course:\*\* UCS654 - Predictive Data Analytics



\*\*Assignment:\*\* TOPSIS Multi-Criteria Decision Making



---



\## Assignment Components



This repository contains all three required parts of the TOPSIS assignment:



\*\*Part I: Command-Line Implementation\*\*

\- File: topsis.py

\- Status: Complete



\*\*Part II: PyPI Package\*\*

\- Package Name: Topsis-Naman-102317144

\- PyPI Link: https://pypi.org/project/Topsis-Naman-102317144/

\- Status: Published and Live



\*\*Part III: Web Service\*\*

\- Files: app.py and templates/index.html

\- Status: Complete



---



\## Part I - Command-Line Tool



\*\*Description\*\*



Standalone Python script for TOPSIS analysis with comprehensive error handling.



\*\*Usage\*\*

```bash

python topsis.py <InputFile> <Weights> <Impacts> <OutputFile>

```



\*\*Example\*\*

```bash

python topsis.py data.csv "1,1,1,1,1" "+,+,-,+,+" result.csv

```



\*\*Features\*\*

\- File existence validation

\- Numeric value checking

\- Parameter count verification

\- Impact direction validation

\- Supports CSV and Excel files



\*\*Input Format\*\*

```csv

Fund Name,P1,P2,P3,P4,P5

M1,0.84,0.71,6.7,42.1,12.59

M2,0.91,0.83,7.0,31.7,10.11

```



\*\*Output Format\*\*



The program adds two new columns:

\- Topsis Score: Calculated performance score

\- Rank: Ranking based on score (1 is best)



---



\## Part II - PyPI Package



\*\*Package Information\*\*



Name: Topsis-Naman-102317144



Version: 1.0.3



PyPI URL: https://pypi.org/project/Topsis-Naman-102317144/



\*\*Installation\*\*

```bash

pip install Topsis-Naman-102317144

```



\*\*Usage After Installation\*\*



Command Line:

```bash

topsis data.csv "1,1,1,1,1" "+,+,-,+,+" output.csv

```



Python Code:

```python

from Topsis\_Naman\_102317144 import run\_topsis



run\_topsis('data.csv', '1,1,1,1,1', '+,+,-,+,+', 'output.csv')

```



\*\*Package Structure\*\*



The package contains:

\- \_\_init\_\_.py - Package initialization

\- \_\_main\_\_.py - Command-line entry point  

\- topsis\_calc.py - Core TOPSIS algorithm



\*\*Verification\*\*



Visit PyPI to verify the package: https://pypi.org/project/Topsis-Naman-102317144/



---



\## Part III - Web Service



\*\*Description\*\*



Flask-based web application with email delivery functionality.



\*\*Files\*\*

\- app.py - Flask application

\- templates/index.html - Web interface



\*\*Running the Service\*\*

```bash

pip install -r requirements.txt

python app.py

```



Then visit: http://localhost:5000



\*\*Features\*\*

\- File upload supporting CSV and Excel

\- Weight and impact input

\- Email address validation

\- Result delivery via email

\- Modern responsive UI



\*\*Email Configuration\*\*



Update app.py lines 114-115 with Gmail credentials:

```python

sender\_email = "your.email@gmail.com"

sender\_password = "your\_app\_password"

```



---



\## Parameters Explanation



\*\*Weights\*\*



Comma-separated numbers representing importance of each criterion.



Example: "1,2,1,1" means the second criterion has double weight



\*\*Impacts\*\*



Comma-separated signs indicating criterion type.



Plus sign means benefit (higher is better)



Minus sign means cost (lower is better)



Example: "+,+,-,+" means the third criterion is cost, others are benefits



---



\## Testing



\*\*Test Part I\*\*

```bash

python topsis.py data.csv "1,1,1,1,1" "+,+,-,+,+" test\_output.csv

```



\*\*Test Part II\*\*

```bash

pip install Topsis-Naman-102317144

topsis data.csv "1,1,1,1,1" "+,+,-,+,+" test\_output2.csv

```



\*\*Test Part III\*\*

```bash

python app.py

```

Open browser and go to: http://localhost:5000



---



\## Dependencies



Required packages:

\- pandas version 1.0.0 or higher

\- numpy version 1.18.0 or higher

\- Flask version 2.0.0 or higher

\- openpyxl version 3.0.0 or higher



Install all dependencies:

```bash

pip install -r requirements.txt

```



---



\## Repository Structure



\*\*Part I - Command-Line\*\*

\- topsis.py



\*\*Part II - PyPI Package Source\*\*

\- Topsis-Naman-102317144 folder containing \_\_init\_\_.py, \_\_main\_\_.py, topsis\_calc.py

\- setup.py

\- setup.cfg

\- MANIFEST.in



\*\*Part III - Web Service\*\*

\- app.py

\- templates folder containing index.html



\*\*Supporting Files\*\*

\- requirements.txt

\- LICENSE.txt

\- data.csv (sample data)

\- test\_topsis.py



---



\## Submission Links



\*\*GitHub Repository (Contains All Parts)\*\*



https://github.com/Naman-Singh-777/topsis-naman-102317144



\*\*PyPI Package (Part II)\*\*



https://pypi.org/project/Topsis-Naman-102317144/



---



\## License



MIT License - See LICENSE.txt for details



---



\## Author



Naman Singh



Roll Number: 102317144



Email: nsingh1\_be23@thapar.edu



---



All three parts are complete, tested, and ready for evaluation.

