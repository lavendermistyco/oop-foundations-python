# OOP Foundations (Python) — Class, Object, Attributes, `__init__`

This repository accompanies an introductory lesson on Object-Oriented Programming (OOP) in Python.  
It includes runnable code examples, lightweight tests, and UML class diagrams (PlantUML) for reference.

---

## 🚀 Quick Setup

1. Install **VS Code** and **Python 3.12.2**.  
2. Open a **Bash terminal** in VS Code.
3. Fork the repo:
   ```bash
      https://github.com/lavendermistyco/oop-foundations-python.git
   ```
5. Clone your forked repo:  
   ```bash
   git clone https://github.com/{YOUR_USERNAME}/oop-foundations-python.git
   cd oop-foundations-python/oop-foundations-student
   ```
6. Create and activate a virtual environment:  
   ```bash
   # On Windows
   py -m venv venv
   source venv/Scripts/activate     # (Git Bash)
   venv\Scripts\Activate.ps1        # (PowerShell)

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```
7. Install packages:  
   ```bash
   pip install pytest
   ```

> 👉 Full step-by-step instructions are in [OOP_Foundations_Setup_Checklist.md](oop-foundations-student/OOP_Foundations_Setup_Checklist.md).

---

## 📚 What You’ll Learn
- Define classes and instantiate objects  
- Use instance attributes and methods  
- Understand and use the `__init__` constructor  
- Read simple UML class diagrams and translate them to code  

---

## 📂 Repository Structure
```
.
├── examples
│   ├── car.py
│   ├── student.py
│   ├── bank_account.py   # scaffolded for you to complete
│   └── library           # breakout UML activity (not code)
├── tests
│   ├── test_bank_account.py
│   └── test_student.py
└── uml
    ├── bank_account.puml
    └── library.puml
```

---

## 🧪 Running Code and Tests
- Run examples:  
  ```bash
  python examples/car.py
  python examples/student.py
  ```
- Run all tests:  
  ```bash
  python -m pytest -q
  ```

---

## 🎯 Breakout Assignments
- `examples/library/` contains **class stubs only** — these are for UML breakout activities, not pre-written solutions.  
- **BankAccount** is your applied coding exercise. It is scaffolded and should be implemented to make the tests pass.  

---
