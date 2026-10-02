"""
Bank Management System
======================
A simple menu-driven console program for managing bank accounts.
This is an educational simulation — not a real banking application.

Features:
  1. Create a new bank account
  2. Deposit money
  3. Withdraw money
  4. Check account balance
  5. Display all accounts
  6. Exit

Data is saved to 'accounts.json' in the same folder so it
persists between program runs.
"""

import json
import os

# ---------------------------------------------------------------------------
# Helper: figure out the path to accounts.json (same folder as this script)
# ---------------------------------------------------------------------------
DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "accounts.json")


# ---------------------------------------------------------------------------
# Load & Save functions
# ---------------------------------------------------------------------------

def load_accounts():
    """Load account data from the JSON file. Return an empty dict if the
    file doesn't exist or is empty."""
    if not os.path.exists(DATA_FILE):
        return {}

    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            # The file might contain an empty list/dict or be truly empty
            if isinstance(data, dict):
                return data
            return {}
    except (json.JSONDecodeError, ValueError):
        # File exists but is empty or has bad JSON — start fresh
        return {}


def save_accounts(accounts):
    """Save the accounts dictionary to the JSON file (pretty-printed)."""
    with open(DATA_FILE, "w") as file:
        json.dump(accounts, file, indent=4)


# ---------------------------------------------------------------------------
# Feature functions
# ---------------------------------------------------------------------------

def create_account(accounts):
    """Create a new bank account with a customer name and account number."""
    print("\n--- Create New Account ---")

    # Get account number
    acc_number = input("Enter account number: ").strip()
    if not acc_number:
        print("❌ Account number cannot be empty.")
        return

    # Check if the account already exists
    if acc_number in accounts:
        print(f"❌ Account number '{acc_number}' already exists.")
        return

    # Get customer name
    name = input("Enter customer name: ").strip()
    if not name:
        print("❌ Customer name cannot be empty.")
        return

    # Create the account with a starting balance of 0
    accounts[acc_number] = {
        "name": name,
        "balance": 0.0
    }
    save_accounts(accounts)
    print(f"✅ Account created successfully for '{name}' (Account #{acc_number}).")


def deposit_money(accounts):
    """Deposit money into an existing account."""
    print("\n--- Deposit Money ---")

    acc_number = input("Enter account number: ").strip()
    if acc_number not in accounts:
        print(f"❌ Account '{acc_number}' not found.")
        return

    try:
        amount = float(input("Enter amount to deposit: "))
    except ValueError:
        print("❌ Invalid amount. Please enter a number.")
        return

    if amount <= 0:
        print("❌ Deposit amount must be greater than zero.")
        return

    accounts[acc_number]["balance"] += amount
    save_accounts(accounts)

    holder = accounts[acc_number]["name"]
    new_balance = accounts[acc_number]["balance"]
    print(f"✅ ₹{amount:.2f} deposited successfully into {holder}'s account.")
    print(f"   Updated balance: ₹{new_balance:.2f}")


def withdraw_money(accounts):
    """Withdraw money from an existing account (cannot exceed balance)."""
    print("\n--- Withdraw Money ---")

    acc_number = input("Enter account number: ").strip()
    if acc_number not in accounts:
        print(f"❌ Account '{acc_number}' not found.")
        return

    current_balance = accounts[acc_number]["balance"]
    print(f"   Current balance: ₹{current_balance:.2f}")

    try:
        amount = float(input("Enter amount to withdraw: "))
    except ValueError:
        print("❌ Invalid amount. Please enter a number.")
        return

    if amount <= 0:
        print("❌ Withdrawal amount must be greater than zero.")
        return

    if amount > current_balance:
        print("❌ Insufficient balance! Withdrawal cancelled.")
        return

    accounts[acc_number]["balance"] -= amount
    save_accounts(accounts)

    holder = accounts[acc_number]["name"]
    new_balance = accounts[acc_number]["balance"]
    print(f"✅ ₹{amount:.2f} withdrawn successfully from {holder}'s account.")
    print(f"   Updated balance: ₹{new_balance:.2f}")


def check_balance(accounts):
    """Display the balance of a specific account."""
    print("\n--- Check Balance ---")

    acc_number = input("Enter account number: ").strip()
    if acc_number not in accounts:
        print(f"❌ Account '{acc_number}' not found.")
        return

    holder = accounts[acc_number]["name"]
    balance = accounts[acc_number]["balance"]
    print(f"   Account #  : {acc_number}")
    print(f"   Name       : {holder}")
    print(f"   Balance    : ₹{balance:.2f}")


def display_all_accounts(accounts):
    """Display a table of every account in the system."""
    print("\n--- All Accounts ---")

    if not accounts:
        print("   No accounts found. Create one first!")
        return

    # Print a simple table header
    print(f"   {'Account #':<15} {'Name':<25} {'Balance':>12}")
    print("   " + "-" * 54)

    for acc_number, info in accounts.items():
        name = info["name"]
        balance = info["balance"]
        print(f"   {acc_number:<15} {name:<25} ₹{balance:>10.2f}")

    print(f"\n   Total accounts: {len(accounts)}")


# ---------------------------------------------------------------------------
# Main menu loop
# ---------------------------------------------------------------------------

def show_menu():
    """Print the main menu options."""
    print("\n" + "=" * 40)
    print("   BANK MANAGEMENT SYSTEM")
    print("=" * 40)
    print("   1. Create Account")
    print("   2. Deposit Money")
    print("   3. Withdraw Money")
    print("   4. Check Balance")
    print("   5. Display All Accounts")
    print("   6. Exit")
    print("=" * 40)


def main():
    """Entry point — runs the menu loop until the user chooses to exit."""
    # Load existing accounts from file (or start with an empty dict)
    accounts = load_accounts()

    print("\nWelcome to the Bank Management System!")
    print("(Educational simulation — not a real bank)\n")

    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            create_account(accounts)
        elif choice == "2":
            deposit_money(accounts)
        elif choice == "3":
            withdraw_money(accounts)
        elif choice == "4":
            check_balance(accounts)
        elif choice == "5":
            display_all_accounts(accounts)
        elif choice == "6":
            print("\nThank you for using the Bank Management System. Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Please enter a number from 1 to 6.")


# Run the program
if __name__ == "__main__":
    main()
