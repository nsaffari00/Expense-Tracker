# Function to add an expense
def add_expense(expenses, category, amount, date):
    try:
        amount = float(amount)  # Ensure the amount is a float
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        expense = {'category': category, 'amount': amount, 'date': date}
        expenses.append(expense)
        print(f"Expense added: {expense}")
    except ValueError as e:
        print(f"Error: {e}")

# Function to view all expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
    else:
        for expense in expenses:
            print(f"Category: {expense['category']}, Amount: {expense['amount']}, Date: {expense['date']}")

# Function to calculate total expenses
def calculate_total(expenses):
    total = sum(expense['amount'] for expense in expenses)
    return total

# Function to filter expenses by category
def filter_expenses(expenses, category):
    filtered = [expense for expense in expenses if expense['category'] == category]
    return filtered

# Function to delete an expense
def delete_expense(expenses, category, date):
    expenses[:] = [expense for expense in expenses if not (expense['category'] == category and expense['date'] == date)]
    print(f"Deleted expenses for category {category} on date {date}.")

# Function to summarize expenses by month
def summarize_by_month(expenses):
    from collections import defaultdict
    monthly_summary = defaultdict(float)
    for expense in expenses:
        month = datetime.strptime(expense['date'], '%Y-%m-%d').strftime('%Y-%m')
        monthly_summary[month] += expense['amount']
    return monthly_summary

# Main program loop
def main():
    expenses = []
    
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total Expenses")
        print("4. Filter Expenses by Category")
        print("5. Delete Expense")
        print("6. Summary by Month")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            category = input("Enter category: ")
            amount = input("Enter amount: ")
            date = input("Enter date (YYYY-MM-DD): ")
            add_expense(expenses, category, amount, date)
        
        elif choice == '2':
            view_expenses(expenses)
        
        elif choice == '3':
            total = calculate_total(expenses)
            print(f"Total Expenses: {total}")
        
        elif choice == '4':
            category = input("Enter category to filter by: ")
            filtered = filter_expenses(expenses, category)
            if filtered:
                print("Filtered Expenses:")
                for expense in filtered:
                    print(f"Category: {expense['category']}, Amount: {expense['amount']}, Date: {expense['date']}")
            else:
                print(f"No expenses found for category {category}.")
        
        elif choice == '5':
            category = input("Enter category to delete: ")
            date = input("Enter date (YYYY-MM-DD) of expense to delete: ")
            delete_expense(expenses, category, date)
        
        elif choice == '6':
            summary = summarize_by_month(expenses)
            if summary:
                print("Monthly Summary:")
                for month, total in summary.items():
                    print(f"{month}: {total}")
            else:
                print("No expenses to summarize.")
        
        elif choice == '7':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

