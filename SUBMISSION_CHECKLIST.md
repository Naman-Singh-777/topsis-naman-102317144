# Assignment Submission Checklist

## Part I: Command-Line TOPSIS Implementation ✓

### Files Required:
- [x] `topsis.py` - Main program file
- [x] Sample input file (`data.csv`)
- [x] Sample output file (`result.csv`)

### Functionality Checklist:
- [x] Accepts 4 command-line parameters
- [x] Validates correct number of parameters
- [x] Shows appropriate error messages
- [x] Handles "File not Found" exception
- [x] Validates minimum 3 columns in input
- [x] Handles non-numeric values
- [x] Validates weights/impacts count matches columns
- [x] Validates impacts are +ve or -ve
- [x] Validates comma separation

### Testing:
```bash
# Test 1: Normal execution
python topsis.py data.csv "1,1,1,1,1" "+,+,-,+,+" result.csv
✓ Creates result.csv with Topsis Score and Rank

# Test 2: Missing parameters
python topsis.py
✓ Shows error message and usage

# Test 3: File not found
python topsis.py missing.csv "1,1" "+,+" out.csv
✓ Shows "File not found" error

# Test 4: Mismatched counts
python topsis.py data.csv "1,1" "+,+,-,+,+" result.csv
✓ Shows error about mismatched counts
```

---

## Part II: PyPI Package ✓

### Package Structure:
- [x] `Topsis-Naman-102317144/` directory
- [x] `__init__.py` with imports
- [x] `__main__.py` for CLI entry point
- [x] `topsis_calc.py` with main logic
- [x] `setup.py` with package metadata
- [x] `setup.cfg` configuration
- [x] `README.md` with usage instructions
- [x] `LICENSE.txt` (MIT License)
- [x] `MANIFEST.in` for including files
- [x] `requirements.txt` with dependencies

### Naming Convention:
- [x] Package name: `Topsis-Naman-102317144`
- [x] Format: Topsis-FirstName-RollNumber

### Documentation:
- [x] User Manual provided (`USER_MANUAL.md`)
- [x] Installation instructions
- [x] Usage examples (CLI and Python)
- [x] Input/output format explained

### PyPI Upload Steps:
1. Create account at pypi.org
2. Install twine: `pip install twine`
3. Build package: `python setup.py sdist bdist_wheel`
4. Upload: `twine upload dist/*`
5. Verify: Visit https://pypi.org/project/Topsis-Naman-102317144/
6. Test install: `pip install Topsis-Naman-102317144`

### Command-Line Testing:
```bash
# After pip install
topsis data.csv "1,1,1,1,1" "+,+,-,+,+" result.csv
✓ Works from anywhere in terminal
```

---

## Part III: Web Service ✓

### Files Required:
- [x] `app.py` - Flask application
- [x] `templates/index.html` - Web interface
- [x] `requirements.txt` - Dependencies

### Functionality:
- [x] User can upload file (CSV/Excel)
- [x] User can input weights (comma-separated)
- [x] User can input impacts (comma-separated)
- [x] User can input email address
- [x] Validates number of weights = number of impacts
- [x] Validates impacts are +ve or -ve
- [x] Validates comma separation
- [x] Validates email format
- [x] Sends result file via email

### Web Interface Features:
- [x] Clean, modern UI
- [x] Form validation
- [x] Error messages displayed
- [x] Success confirmation
- [x] Instructions provided
- [x] File upload support (CSV, Excel)

### Email Configuration:
```python
# In app.py, update:
sender_email = "your_email@gmail.com"
sender_password = "your_app_password"
```

### Testing Web Service:
```bash
# Start server
python app.py

# Open browser
http://localhost:5000

# Test:
1. Upload data.csv
2. Enter weights: 1,1,1,1,1
3. Enter impacts: +,+,-,+,+
4. Enter email: test@example.com
5. Click Submit
✓ Result sent to email
```

---

## GitHub Repository

### Required Files:
- [x] All source code files
- [x] README.md (project overview)
- [x] LICENSE.txt
- [x] requirements.txt
- [x] Sample data files
- [x] Documentation

### Repository Structure:
```
topsis-package/
├── Topsis-Naman-102317144/     # Package
├── templates/                   # Web templates
├── topsis.py                    # Standalone CLI
├── app.py                       # Web service
├── setup.py
├── README.md
├── USER_MANUAL.md
├── LICENSE.txt
├── requirements.txt
├── data.csv                     # Sample data
└── result.csv                   # Sample output
```

### GitHub Upload:
1. Create repository: `topsis-aryan-102317144`
2. Add all files
3. Commit with message: "Complete TOPSIS implementation"
4. Push to GitHub
5. Add brief description in repo settings

---

## Final Submission

### What to Submit:

**1. GitHub Link:**
- URL: https://github.com/your-username/topsis-aryan-102317144
- Must include all three parts
- Must have README with usage instructions

**2. PyPI Link:**
- URL: https://pypi.org/project/Topsis-Naman-102317144/
- Package must be installable via pip
- Must have description and examples

**3. Documentation:**
- README.md in GitHub
- User Manual
- Sample data and results

**4. Demo/Screenshots (Optional but Good):**
- Screenshot of CLI usage
- Screenshot of web interface
- Screenshot of email received

---

## Pre-Submission Verification

### Quick Test All Parts:

```bash
# Part I: CLI
python topsis.py data.csv "1,1,1,1,1" "+,+,-,+,+" result.csv
cat result.csv  # Verify output

# Part II: Package
pip install Topsis-Naman-102317144
topsis data.csv "1,1,1,1,1" "+,+,-,+,+" result2.csv

# Part III: Web
python app.py
# Test in browser at localhost:5000
```

---

## Common Issues to Avoid

❌ **Wrong package naming**
- Use exact format: `Topsis-FirstName-RollNumber`

❌ **Missing error handling**
- Test all error cases before submission

❌ **No user manual**
- Provide clear usage instructions

❌ **Broken PyPI package**
- Test installation before submitting link

❌ **Email not configured**
- Update sender credentials in app.py

❌ **Missing dependencies**
- Include all in requirements.txt

---

## Grading Criteria (Reference)

### Part I (40%):
- Correct TOPSIS implementation
- Proper error handling
- Code quality and comments
- Testing and validation

### Part II (30%):
- Package structure
- PyPI upload successful
- Documentation quality
- Naming convention followed

### Part III (30%):
- Web interface functionality
- Email delivery working
- Input validation
- UI/UX quality

---

## Final Checklist

Before submitting:

- [ ] All code files tested and working
- [ ] Package uploaded to PyPI successfully
- [ ] Can install via `pip install Topsis-Naman-102317144`
- [ ] GitHub repository created and pushed
- [ ] README.md is comprehensive
- [ ] User manual provided
- [ ] Web service tested locally
- [ ] Email functionality configured
- [ ] All error cases handled
- [ ] Sample data and results included
- [ ] Code is clean and commented
- [ ] No hardcoded paths or credentials (in GitHub)

---

**READY TO SUBMIT! 🎉**

Make sure to:
1. Push everything to GitHub
2. Verify PyPI package works
3. Test all three parts one final time
4. Submit GitHub link as instructed
