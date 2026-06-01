#  1. Take two numbers as input
# We use float() so the calculator can handle both integers and decimals
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# 2. Arithmetic Operators
print("\n=== Arithmetic Operators ===")
print(f"Addition ({num1} + {num2}):", num1 + num2)
print(f"Subtraction ({num1} - {num2}):", num1 - num2)
print(f"Multiplication ({num1} * {num2}):", num1 * num2)

# Handling division by zero safely
if num2 != 0:
    print(f"Division ({num1} / {num2}):", num1 / num2)
    print(f"Modulus/Remainder ({num1} % {num2}):", num1 % num2)
else:
    print("Division and Modulus: Cannot divide by zero!")

print(f"Exponentiation ({num1} ** {num2}):", num1 ** num2)

# 3. Comparison Operators
print("\n=== Comparison Operators ===")
print(f"Is Equal (==): {num1 == num2}")
print(f"Not Equal (!=): {num1 != num2}")
print(f"Greater Than (>): {num1 > num2}")
print(f"Less Than (<): {num1 < num2}")
print(f"Greater or Equal (>=): {num1 >= num2}")
print(f"Less or Equal (<=): {num1 <= num2}")

# 4. Logical Operators
print("\n=== Logical Operators ===")
# Example conditions to evaluate True/False values
condition1 = num1 > 0
condition2 = num2 > 0

print(f"Condition 1 (Is num1 positive?): {condition1}")
print(f"Condition 2 (Is num2 positive?): {condition2}")
print(f"AND (Are BOTH positive?): {condition1 and condition2}")
print(f"OR (Is AT LEAST ONE positive?): {condition1 or condition2}")
print(f"NOT (Is num1 NOT positive?): {not condition1}")