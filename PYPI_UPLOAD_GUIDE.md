# How to Upload to PyPI

## Prerequisites

1. Create PyPI account at https://pypi.org/account/register/
2. Verify your email
3. Remember your username and password

## Step 1: Install Required Tools

```bash
pip install twine
pip install wheel
pip install setuptools
```

## Step 2: Prepare Your Package

Make sure you're in the project directory:

```bash
cd topsis_project
```

Check that all required files exist:
- ✓ setup.py
- ✓ setup.cfg
- ✓ README.md
- ✓ LICENSE.txt
- ✓ MANIFEST.in
- ✓ Topsis-Naman-102317144/ (package folder)

## Step 3: Create Distribution Files

```bash
python setup.py sdist bdist_wheel
```

This creates:
- `dist/Topsis-Naman-102317144-1.0.3.tar.gz` (source distribution)
- `dist/Topsis_Naman_102317144-1.0.3-py3-none-any.whl` (wheel)

## Step 4: Test on TestPyPI (Optional but Recommended)

First, register at https://test.pypi.org/account/register/

Upload to TestPyPI:

```bash
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

Enter your TestPyPI username and password when prompted.

Test installation:

```bash
pip install --index-url https://test.pypi.org/simple/ Topsis-Naman-102317144
```

## Step 5: Upload to PyPI

```bash
twine upload dist/*
```

Enter your PyPI username and password when prompted.

## Step 6: Verify Upload

Visit: https://pypi.org/project/Topsis-Naman-102317144/

You should see your package!

## Step 7: Install and Test

```bash
pip install Topsis-Naman-102317144

# Test it
topsis --help
```

## Updating Your Package

When you make changes:

1. Update version in `setup.py` and `__init__.py`
   ```python
   version="1.0.4",  # Increment version
   ```

2. Remove old distributions:
   ```bash
   rm -rf dist/ build/ *.egg-info
   ```

3. Create new distribution:
   ```bash
   python setup.py sdist bdist_wheel
   ```

4. Upload new version:
   ```bash
   twine upload dist/*
   ```

## Troubleshooting

### Error: "File already exists"
- You're trying to upload a version that already exists
- Update version number in setup.py

### Error: "Invalid username/password"
- Double-check credentials
- For Gmail, use App Password, not regular password

### Error: "Package name already taken"
- Someone else registered that name
- Choose a different name
- Current name: Topsis-Naman-102317144

### Error: "Long description has syntax errors"
- Check README.md is valid Markdown
- Make sure it's UTF-8 encoded

## Using API Token (More Secure)

1. Go to https://pypi.org/manage/account/
2. Scroll to "API tokens"
3. Create token with scope "Entire account"
4. Create `~/.pypirc`:

```ini
[pypi]
username = __token__
password = pypi-YOUR-TOKEN-HERE
```

5. Upload:
```bash
twine upload dist/*
```

## Quick Reference

```bash
# Full upload process
rm -rf dist/ build/ *.egg-info
python setup.py sdist bdist_wheel
twine check dist/*
twine upload dist/*
```

## After Upload

Update your GitHub README with:

```markdown
## Installation

pip install Topsis-Naman-102317144
```

Share your package:
- Link: https://pypi.org/project/Topsis-Naman-102317144/
- Command: `pip install Topsis-Naman-102317144`
