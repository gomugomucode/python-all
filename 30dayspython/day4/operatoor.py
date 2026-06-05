# =========================================
# Operator Precedence & Associativity Demo
# =========================================

print("=== 1. * and / before + and - ===")

print("2 + 3 * 4 =", 2 + 3 * 4)  
# Expected: 14 | Multiplication happens before addition

print("(2 + 3) * 4 =", (2 + 3) * 4)  
# Expected: 20 | Parentheses override precedence


print("\n=== 2. Exponentiation and unary minus ===")

print("2 ** 3 ** 2 =", 2 ** 3 ** 2)  
# Expected: 512 | Right-associative: 2 ** (3 ** 2)

print("-3 ** 2 =", -3 ** 2)  
# Expected: -9 | ** happens before unary minus


print("\n=== 3. Left-to-right associativity ===")

print("100 / 5 * 2 =", 100 / 5 * 2)  
# Expected: 40.0 | Same precedence, evaluated left to right

print("10 - 5 - 2 =", 10 - 5 - 2)  
# Expected: 3 | Subtraction is left-associative


print("\n=== 4. Mixed arithmetic + comparison + logic ===")

print("5 + 3 > 7 and not 2 > 5 =", 5 + 3 > 7 and not 2 > 5)  
# Expected: True | Arithmetic first, then comparison, then NOT, then AND


print("\n=== END ===")