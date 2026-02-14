# 📧 Email Configuration Guide - Naman Singh

## ✅ Email Updated Everywhere

Your email **nsingh1_be23@thapar.edu** has been updated in:

- ✅ `setup.py` (Package author email)
- ✅ All documentation files
- ✅ `app.py` (Web service sender email)
- ✅ README files
- ✅ User manual

---

## 🔧 For Web Service Email Functionality

### Important: Gmail Setup Required

**The Thapar email (nsingh1_be23@thapar.edu) may not work directly for sending emails** through the web service because:
- Thapar email might not support SMTP access
- Gmail is recommended for SMTP email sending

### Option 1: Use Gmail (Recommended)

If you have a Gmail account, use it for the web service:

**Update in `app.py` (lines 114-115):**

```python
sender_email = "your.gmail@gmail.com"  # Your Gmail
sender_password = "your_app_password"   # Gmail App Password
```

**How to get Gmail App Password:**

1. Go to Google Account: https://myaccount.google.com
2. Security → 2-Step Verification (enable it)
3. Security → App Passwords
4. Select app: "Mail"
5. Select device: "Other" (type: TOPSIS App)
6. Click "Generate"
7. Copy the 16-character password
8. Use that in `app.py`

### Option 2: Use Thapar Email (If SMTP Available)

Check if Thapar provides SMTP access:

**If yes, update `app.py` line 153:**

```python
# Change from:
server = smtplib.SMTP('smtp.gmail.com', 587)

# To Thapar SMTP (check with IT department):
server = smtplib.SMTP('smtp.thapar.edu', 587)  # Example - verify actual server
```

### Option 3: Skip Email Feature

If you don't want email functionality:
- Keep the code as is
- The web service will show an error message
- Users can still see results in browser
- Mention in documentation: "Email feature under development"

---

## 📦 Current Status

### Package Metadata (PyPI)
```python
# setup.py
author="Naman Singh"
author_email="nsingh1_be23@thapar.edu"
```
✅ This is perfect - shows on PyPI as your contact

### Web Service Email
```python
# app.py (lines 114-115)
sender_email = "nsingh1_be23@thapar.edu"
sender_password = "your_app_password"
```
⚠️ **Action Required:** Update password before using web service

---

## 🚀 What You Should Do

### Before Submitting to PyPI:
✅ **Nothing to change** - email is already set correctly

### Before Using Web Service:
Choose one:

**A. Use Gmail for sending (Easiest):**
```python
# In app.py, line 114-115
sender_email = "yourgmail@gmail.com"
sender_password = "abcd efgh ijkl mnop"  # 16-char App Password
```

**B. Use Thapar email (If SMTP available):**
1. Contact Thapar IT for SMTP settings
2. Update server settings in app.py
3. Update password

**C. Disable email temporarily:**
- Leave as is
- Comment in documentation: "Email feature coming soon"
- Web UI will still work, just no email delivery

---

## 📝 Quick Reference

**Your Details:**
- Name: Naman Singh
- Roll: 102317144
- Email: nsingh1_be23@thapar.edu
- Package: Topsis-Naman-102317144

**Email Usage:**
- ✅ PyPI/Documentation: nsingh1_be23@thapar.edu (done!)
- ⚠️ Web Service Sender: Update in app.py before deploying

---

## ⚡ Quick Test

To test if current email works for sending:

```python
import smtplib

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('nsingh1_be23@thapar.edu', 'your_password')
    print("✓ Email configured correctly!")
except Exception as e:
    print(f"✗ Error: {e}")
    print("Use Gmail instead or check SMTP settings")
```

---

## 💡 Recommendation

**For Assignment Submission:**
- ✅ Keep Thapar email in package metadata (already done)
- ✅ Either:
  - Setup Gmail for web service, OR
  - Mention "Email feature requires Gmail setup" in docs

**This way:**
- Your Thapar email shows on PyPI ✓
- Web service can work with Gmail ✓
- Everything is professional ✓

---

## 🎯 Bottom Line

✅ **Package email: DONE** - Your Thapar email is everywhere  
⚠️ **Web service: YOUR CHOICE** - Update app.py if you want email to work

**For now, you can submit without changing anything else!**

The email functionality is optional - the main TOPSIS features work perfectly without it.

---

**Need help with Gmail App Password? Check the steps above!** 📧
