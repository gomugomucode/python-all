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

    print(load_expenses(notebooks/expenses.txt))
        
        