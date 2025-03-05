import csv
import os
from datetime import datetime

# File to store expenses
FILE_NAME = "expenses.csv"

# Function to initialize the CSV file if not present
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])

# Function to add an expense
def add_expense():
    date = datetime.now().strftime('%Y-%m-%d')
    category = input("Enter category (Food, Transport, Entertainment, etc.): ").strip()
    try:
        amount = float(input("Enter amount spent: ").strip())
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return
    description = input("Enter a brief description: ").strip()
    
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    print("Expense added successfully!")

# Function to display all expenses
def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses recorded yet.")
        return
    
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        if len(rows) <= 1:
            print("No expenses recorded yet.")
            return
        
        print("\nDate | Category | Amount | Description")
        print("-" * 50)
        for row in rows[1:]:  # Skip header
            if len(row) < 4:  # Ensure the row is complete
                print(f"Skipping invalid row: {row}")
                continue
            try:
                amount = float(row[2])  # Convert amount safely
                print(f"{row[0]} | {row[1]} | ${amount:.2f} | {row[3]}")
            except ValueError:
                print(f"Skipping corrupted row: {row}")

# Function to show summary by category
def expense_summary():
    if not os.path.exists(FILE_NAME):
        print("No expenses recorded yet.")
        return
    
    expenses = {}
    total = 0
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip header row
        for row in reader:
            if len(row) < 3:  # Skip incomplete rows
                continue
            try:
                category, amount = row[1], float(row[2])
                expenses[category] = expenses.get(category, 0) + amount
                total += amount
            except ValueError:
                print(f"Skipping invalid entry: {row}")
    
    if not expenses:
        print("No valid expenses recorded yet.")
        return
    
    print("\nExpense Summary:")
    print("-" * 25)
    for category, amount in expenses.items():
        print(f"{category}: ${amount:.2f}")
    print(f"Total Spent: ${total:.2f}")

# Main function to run the expense tracker
def main():
    initialize_file()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Expense Summary")
        print("4. Exit")
        
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            expense_summary()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
