import math
import random
import datetime

# 1. Generate a random integer between 1 and 100
random_num = random.randint(1, 100)
print(f"Random Number Generated: {random_num}")

# 2. Calculate and print the square root
square_root = math.sqrt(random_num)
print(f"Square Root of {random_num}: {square_root:.4f}")  # Formatted to 4 decimal places

# 3. Fetch and print the current date and time
current_datetime = datetime.datetime.now()
print(f"Raw Date and Time: {current_datetime}")

# Extra: Clean formatting for readability
formatted_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted Date and Time: {formatted_date}")
