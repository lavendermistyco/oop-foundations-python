# 🛠️ Setup Checklist for OOP Foundations

Please complete these steps **before class** so we can dive right into coding.  

---

## ✅ 1. Install VS Code
- Download from [https://code.visualstudio.com](https://code.visualstudio.com)  
- Install with default settings.  
- Open it once to confirm it works.  

---

## ✅ 2. Install Python 3.12.2
- Download from [python.org/downloads](https://www.python.org/downloads/release/python-3122/).  
- During installation:  
  - **Check the box** that says *“Add Python to PATH”*.  
- Confirm installation:  
  ```bash
  python --version
  ```  
  or  
  ```bash
  py -V
  ```  
  should show `Python 3.12.2`.  

---

## ✅ 3. Install Bash for VS Code
- If you’re on **Windows**, install **Git for Windows** (includes Git Bash):  
  [https://git-scm.com/download/win](https://git-scm.com/download/win)  
- Open VS Code → **Terminal** → select **Git Bash**.  

---

## ✅ 4. Clone the Repository
Now that Git Bash is available, download the starter code from GitHub:  

```bash
git clone https://github.com/lavendermistyco/oop-foundations-python.git
cd oop-foundations-python
```

---

## ✅ 5. Create a Virtual Environment (venv)
In your cloned project folder (`oop-foundations-python`):  

### On Windows:
```bash
py -m venv venv
```
(or, if that doesn’t work)
```bash
python -m venv venv
```

### On macOS/Linux:
```bash
python3 -m venv venv
```

---

## ✅ 6. Activate the venv
- **Windows (Git Bash):**
  ```bash
  source venv/Scripts/activate
  ```
- **Windows (PowerShell):**
  ```powershell
  venv\Scripts\Activate.ps1
  ```
- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

You should see `(venv)` at the start of your terminal line.  

---

## ✅ 7. Install pip Packages
Inside the activated venv:  
```bash
pip install pytest
```

Confirm pytest works:  
```bash
pytest --version
```

---

## ✅ 8. VS Code Setup
- Install the **Python extension** by Microsoft in VS Code (from Extensions Marketplace).  
- Press **Ctrl+Shift+P** (Cmd+Shift+P on Mac) → select **Python: Select Interpreter**.  
- Choose the interpreter that points to your new `venv`.  

---

## ✅ 9. Verify Everything Works
From your project folder, run:  
```bash
python -m pytest tests/test_bank_account.py
```
(or, if on Windows and `python` doesn’t work:)
```bash
py -m pytest tests/test_bank_account.py
```

You should see tests running (they may fail at first — that’s expected until you implement the code).  

---

✨ Now you’re ready for class!  
