# A function-based expense tracker that records and summarizes spending.

Define the following functions: 
- add_expense(description, amount) → adds an expense to the log 
- list_expenses() → prints all expenses in a readable table 
- total_expenses() → returns the sum of all amounts 
- export_to_csv(filename) → saves the expenses to a .csv file 

Use a loop to let the user choose actions: Add, List, Total, Export, or Quit. 

Bonus (optional): 
- Add a timestamp to each expense. 
- Format currency to 2 decimal places. 
- Support categories for each entry (e.g., Food, Travel, Bills). 
- Save/load expenses from file on program start.

### ✅ Features:
- Stores expenses as list of dictionaries
- Functions for add, list, total, export
- Categories supported
- CSV persistence (loads on start, saves on quit)
- Currency formatted to 2 decimals

### ✅ Features of GUI:

- Form inputs (Description, Amount, Category)
- Table with scroll to view all expenses
- Add Expense button inserts into table instantly
- Show Total button pops up a summary
- Export CSV button saves all data
- Auto-load previous CSV on startup

### ✅ Improvements

- Categories now selected via dropdown menu (Food, Travel, Bills, Shopping, Health, Entertainment, Other)
- Default value is General
- Auto-resets dropdown after adding an expense