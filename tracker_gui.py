import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
import os

# Global expense list
expenses = []


# Core Functions

def add_expense(description, amount, category="General"):
    """Add an expense entry."""
    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Invalid Input", "Amount must be a number")
        return False

    expense = {
        "description": description,
        "amount": round(amount, 2),
        "category": category
    }
    expenses.append(expense)
    update_table()
    return True


def update_table():
    """Refresh the table with current expenses."""
    for row in tree.get_children():
        tree.delete(row)

    for exp in expenses:
        tree.insert("", tk.END, values=(
            exp["description"],
            exp["category"],
            f"₹{exp['amount']:.2f}"
        ))


def total_expenses():
    """Show total expenses in a message box."""
    total = sum(exp["amount"] for exp in expenses)
    messagebox.showinfo("Total Expenses", f"💰 Total: ₹{total:.2f}")


def export_to_csv(filename="expenses.csv"):
    """Save expenses to a CSV file."""
    if not expenses:
        messagebox.showwarning("No Data", "No expenses to export.")
        return

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["description", "category", "amount"])
        writer.writeheader()
        writer.writerows(expenses)

    messagebox.showinfo("Export Successful", f"Expenses exported to {filename}")


def load_expenses(filename="expenses.csv"):
    """Load expenses from a CSV file if it exists."""
    if os.path.exists(filename):
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["amount"] = float(row["amount"])
                expenses.append(row)
        update_table()


# GUI Setup

root = tk.Tk()
root.title("Expense Tracker")
root.geometry("700x500")

# Input Frame
frame_input = tk.Frame(root, pady=10)
frame_input.pack(fill="x")

tk.Label(frame_input, text="Description").grid(row=0, column=0, padx=5)
entry_desc = tk.Entry(frame_input, width=20)
entry_desc.grid(row=0, column=1, padx=5)

tk.Label(frame_input, text="Amount").grid(row=0, column=2, padx=5)
entry_amount = tk.Entry(frame_input, width=10)
entry_amount.grid(row=0, column=3, padx=5)

tk.Label(frame_input, text="Category").grid(row=0, column=4, padx=5)
entry_category = tk.Entry(frame_input, width=15)
entry_category.grid(row=0, column=5, padx=5)


def on_add():
    desc = entry_desc.get().strip()
    amount = entry_amount.get().strip()
    category = entry_category.get().strip()

    if not desc or not amount:
        messagebox.showwarning("Missing Info", "Please enter description and amount")
        return

    if add_expense(desc, amount, category):
        entry_desc.delete(0, tk.END)
        entry_amount.delete(0, tk.END)
        entry_category.delete(0, tk.END)


btn_add = tk.Button(frame_input, text="Add Expense", command=on_add)
btn_add.grid(row=0, column=6, padx=5)


# Expense Table
frame_table = tk.Frame(root)
frame_table.pack(fill="both", expand=True)

columns = ("Description", "Category", "Amount")
tree = ttk.Treeview(frame_table, columns=columns, show="headings", height=15)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")

tree.pack(fill="both", expand=True, side="left")

scrollbar = ttk.Scrollbar(frame_table, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side="right", fill="y")


# Bottom Buttons
frame_buttons = tk.Frame(root, pady=10)
frame_buttons.pack()

btn_total = tk.Button(frame_buttons, text="Show Total", command=total_expenses)
btn_total.grid(row=0, column=0, padx=10)

btn_export = tk.Button(frame_buttons, text="Export CSV", command=export_to_csv)
btn_export.grid(row=0, column=1, padx=10)

btn_quit = tk.Button(frame_buttons, text="Quit", command=root.quit)
btn_quit.grid(row=0, column=2, padx=10)


if __name__ == '__main__':
    # Load existing expenses
    load_expenses()

    root.mainloop()
