
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
                
            # 2. Split the line into category and amount at the comma
            category, amount = clean_line.split(',')
            
            # 3. Convert the amount to an  float and save as a tuple
            expenses.append((category, int(amount)))
            
    return expenses



# 1. Get the directory where your script is saved
script_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Join that directory path with your filename
filename = os.path.join(script_dir, "expenses.txt")

filename = "expenses.txt"
print(load_expenses(filename))