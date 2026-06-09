import os


def load_expenses(filename):
    expenses = []

    # Open the file in read mode ('r')
    with open(filename, "r") as file:
        for line in file:
            # 1. strip() removes the hidden newline character '\n'
            clean_line = line.strip()

            # Skip empty lines if there are any in the file
            if not clean_line:
                continue

            # 2. Skip lines that are missing a comma
            if "," not in clean_line:
                print(f"Skipping malformed line: '{clean_line}'")
                continue

            # 3. Now it is safe to split!
            category, amount = clean_line.split(",")
            expenses.append((category, int(amount)))

    return expenses


def add_expense(filename, category, amount):
    # Opening with 'a' appends data to the end of the file
    with open(filename) as file:
        # \n ensures the new expense starts on a clean, new line
        file.write(f"{category},{amount}")
        print(f"Successfully added: {category}, {amount}")



def category_totals(expenses):
   # Created an empty dictionary to track totals
    totals = {}
    
    for category, amount in expenses:
        totals[category] = totals.get(category, 0) + amount 

    print("\nCategory totals:")
    print(f"{'Category':<15} | {'Total':<10}")
    print("-" * 28)
    
    for category, total_amount in totals.items():
        print(f"{category:<15} | Rs. {total_amount:<10}")

def above_threshold(expenses, limit):
    totals = {}
    
    # 1. Sum up all expenses by category
    for category, amount in expenses:
        totals[category] = totals.get(category, 0) + amount 
        
    print(f"\nCategories exceeding Rs. {limit}:")
    print(f"{'Category':<15} | {'Total':<10}")
    print("-" * 28)

    # 2. loop to filter and print totals over the limit
    for category, total_amount in totals.items():
        if total_amount > limit:
            print(f"{category:<15} | Rs. {total_amount:<10}")


if __name__ == "__main__":
    # 1. Get the directory where your script is saved
    script_dir = os.path.dirname(
        os.path.abspath(
            "C:\\Users\\Anupam Baral\\Downloads\\python\\30dayspython\\Personal Expense Tracker .py"
        )
    )

    # 2. Join that directory path with your filename
    filename = os.path.join(script_dir, "expenses.txt")
    current_expenses = load_expenses(filename)
    
    if not current_expenses:
        print(f"Warning: No expenses loaded. Please check that '{filename}' exists and has valid data.")
    else:
        category_totals(current_expenses)
        above_threshold(current_expenses, 100)



print(load_expenses(filename))
