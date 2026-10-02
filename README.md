# 🏦 Bank Management System

A simple, menu-driven **console application** built with Python.  
This is a **college mini project** designed as an educational simulation — it does **not** involve real banking, online payments, or sensitive data.

---

## 📌 Project Objective

To demonstrate fundamental Python programming concepts — functions, loops, conditionals, file handling, and dictionaries — through a practical, easy-to-understand project that simulates basic bank account operations.

---

## 🛠️ Tools Used

| Tool              | Purpose                                    |
| ----------------- | ------------------------------------------ |
| **Python 3**      | Programming language                       |
| **json** (stdlib) | Reading and writing account data to a file |
| **os** (stdlib)   | File-path handling                         |

> No external packages or databases are required.

---

## ✨ Features

1. **Create Account** — Register a new customer with a name and account number.
2. **Deposit Money** — Add funds to an existing account.
3. **Withdraw Money** — Remove funds (prevents overdrafts).
4. **Check Balance** — View the balance of a specific account.
5. **Display All Accounts** — See a summary table of every account.
6. **Exit** — Close the program gracefully.

---

## 📂 Project Structure

```
Bank-Management-System/
├── bank_management.py   # Main Python program
├── accounts.json        # Data file (auto-created / updated at runtime)
└── README.md            # This file
```

---

## ⚙️ How It Works

1. When the program starts, it loads account data from `accounts.json`.  
   If the file is empty or missing, it begins with no accounts.
2. The user is shown a numbered menu and picks an option (1–6).
3. Each operation updates an in-memory Python dictionary and immediately saves it back to `accounts.json`, so data is never lost between runs.
4. Basic input validation ensures account numbers aren't duplicated, amounts are positive numbers, and withdrawals don't exceed the available balance.

---

## 🚀 How to Run

### Prerequisites

- **Python 3.6 or newer** installed on your system.  
  Check with: `python --version` (or `python3 --version` on macOS/Linux).

### Steps

1. **Download / extract** the `Bank-Management-System` folder.

2. **Open a terminal** (Command Prompt, PowerShell, or any terminal) and navigate to the project folder:
   ```bash
   cd path/to/Bank-Management-System
   ```

3. **Run the program:**
   ```bash
   python bank_management.py
   ```
   *(Use `python3` instead of `python` if required on your system.)*

4. Follow the on-screen menu to create accounts, deposit, withdraw, and more.

---

## 📸 Sample Output

```
Welcome to the Bank Management System!
(Educational simulation — not a real bank)

========================================
   BANK MANAGEMENT SYSTEM
========================================
   1. Create Account
   2. Deposit Money
   3. Withdraw Money
   4. Check Balance
   5. Display All Accounts
   6. Exit
========================================
Enter your choice (1-6): 1

--- Create New Account ---
Enter account number: 1001
Enter customer name: Alice
✅ Account created successfully for 'Alice' (Account #1001).
```

---

## 📝 Notes

- This project is for **educational purposes only**. It does not implement authentication, encryption, or any real financial logic.
- Account data is stored in plain-text JSON. Do not use this for sensitive information.
- Feel free to extend the project with features like transaction history, interest calculation, or a search function as a learning exercise!

---

## 📜 License

This project is open for academic and personal use. No license restrictions.
