# Cinema Ticket Pricing System

# Input
age = int(input("Enter age: "))
day = input("Enter day of the week: ").strip().lower()
member_input = input("Are you a member? (yes/no): ").strip().lower()

# Convert membership to boolean
is_member = member_input == "yes"

# Base ticket price
full_price = 500

# Age-based pricing
if age < 5:
    final_price = 0
    category = "Under 5"
    age_discount = "100% (Free Entry)"
elif age < 18:
    final_price = full_price * 0.5
    category = "Minor"
    age_discount = "50%"
elif age >= 60:
    final_price = full_price * 0.7
    category = "Senior Citizen"
    age_discount = "30%"
else:
    final_price = full_price
    category = "Adult"
    age_discount = "0%"

# Extra discount for members on weekdays
weekday_discount = 0
weekdays = {"monday", "tuesday", "wednesday", "thursday", "friday"}

if is_member and day in weekdays:
    weekday_discount = final_price * 0.10
    final_price -= weekday_discount

# Nested if for popcorn offer
if final_price == 0:
    popcorn_offer = "Free Small Popcorn"
else:
    if is_member:
        popcorn_offer = "Free Large Popcorn"
    else:
        popcorn_offer = "No Popcorn Offer"

# Ternary expression
message = "Free Entry!" if final_price == 0 else "Enjoy the Show!"

# Output Summary
print("\n===== CINEMA TICKET SUMMARY =====")
print("Category:", category)
print("Age Discount:", age_discount)
print("Member:", is_member)
print("Extra Member Discount: Rs.", round(weekday_discount, 2))
print("Popcorn Offer:", popcorn_offer)
print("Final Price: Rs.", round(final_price, 2))
print("Message:", message)