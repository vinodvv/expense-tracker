import os
import csv


# Global expense list
expenses = []


# Core Functions

def add_expense(description, amount, category="General"):
    """Add an expense entry with description, amount, and category"""
    try:
        amount = float(amount)  # ✅ Always convert to float here
    except ValueError:
        print("❌ Invalid amount. Please enter a number.")
        return

    expense = {
        "description": description,
        "amount": round(amount, 2),  # ✅ Now safe
        "category": category
    }
    expenses.append(expense)
    print(f"✅ Added: {description} - ₹{amount:.2f} ({category})")


def list_expenses():
    """Print all expenses in a readable table"""
    if not expenses:
        print("⚠️ No expenses recorded yet.")
        return

    print("\n--- Expense Log ---")
    print(f"{'Description':15} | {'Category':10} | {'Amount':>8}")
    print("-" * 60)

    for exp in expenses:
        print(f"{exp['description'][:15]:15} | {exp['category'][:10]:10} | ₹{exp['amount']:>7.2f}")

    print("-" * 60)


def total_expenses():
    """Return and print the total expenses."""
    total = sum(exp["amount"] for exp in expenses)
    print(f"💰 Total Expenses: ₹{total:.2f}")
    return total


def export_to_csv(filename="expenses.csv"):
    """Save expenses to a CSV file"""
    if not expenses:
        print("⚠️ No expenses to export.")
        return

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["description", "category", "amount"])
        writer.writeheader()
        writer.writerows(expenses)

    print(f"📂 Expenses exported to {filename}")


def load_expenses(filename="expenses.csv"):
    """Load expenses from a CSV file if it exists."""
    if os.path.exists(filename):
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["amount"] = float(row["amount"])  # Convert amount back to float
                expenses.append(row)
        print(f"📥 Loaded {len(expenses)} expenses from {filename}")


# Main Program Loop

def main():
    load_expenses()  # Load saved expenses at startup

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. List Expenses")
        print("3. Show Total")
        print("4. Export to CSV")
        print("5. Quit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            description = input("Enter description: ").strip()
            amount = input("Enter amount: ").strip()
            category = input("Enter category (Food/Travel/Bills/etc.): ").strip() or "General"
            add_expense(description, amount, category)

        elif choice == "2":
            list_expenses()

        elif choice == "3":
            total_expenses()

        elif choice == "4":
            filename = input("Enter filename (default: expenses.csv): ").strip() or "expenses.csv"
            export_to_csv(filename)

        elif choice == "5":
            print("👋 Goodbye! Expenses saved.")
            export_to_csv()  # Autosave before quitting
            break

        else:
            print("❌ Invalid option. Please try again.")


if __name__ == "__main__":
    main()
