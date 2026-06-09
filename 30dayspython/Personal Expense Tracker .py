
import os
def load_expenses(filename):
    expenses = []
    
    # Open the file in read mode ('r')
    with open(filename, 'r') as file:
        for line in file:
            # 1. strip() removes the hidden newline character '\n'
            clean_line = line.strip()
            
            # Skip empty lines if there are any in the file
            if not clean_line:
                continue
                
            # 2. Skip lines that are missing a comma
            if ',' not in clean_line:
                print(f"Skipping malformed line: '{clean_line}'")
                continue
                
            # 3. Now it is safe to split!
            category, amount = clean_line.split(',')
            expenses.append((category, int(amount)))
            
    return expenses

# 1. Get the directory where your script is saved
script_dir = os.path.dirname(os.path.abspath("C:\\Users\\Anupam Baral\\Downloads\\python\\30dayspython\\Personal Expense Tracker .py"))

# 2. Join that directory path with your filename
filename = os.path.join(script_dir, "expenses.txt")


print(load_expenses(filename))