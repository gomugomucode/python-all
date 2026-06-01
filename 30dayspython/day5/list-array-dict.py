# Create a list of 5 programming languages
languages = ["Python", "JavaScript", "C++", "Java", "Ruby"]

# 1. Add one language
languages.append("Go")

# 2. Remove one language
languages.remove("Ruby")

# 3. Print all languages
print("All languages:")
for lang in languages:
    print(lang)

# 4. Print the total number of languages
print("Total number of languages:", len(languages))


employee = {
    "name": "John",
    "salary": 50000,
    "department": "IT"
}

# 1. Add email
employee["email"] = "john@example.com"

# 2. Update salary
employee["salary"] = 55000

# 3. Delete department
del employee["department"]

# 4. Print all keys
print("Employee Keys:", list(employee.keys()))

# 5. Print all values
print("Employee Values:", list(employee.values()))


# Creating a simple dictionary for a smartphone
phone = {
    "brand": "Apple",
    "model": "iPhone 15",
    "storage_gb": 128,
    "is_5g": True
}

# 1. Accessing data using keys
print("Phone Brand:", phone["brand"])
print("Storage Size:", phone["storage_gb"], "GB")

# 2. Modifying a value
phone["storage_gb"] = 256
print("Updated Storage:", phone["storage_gb"], "GB")

# 3. Adding a new key-value pair
phone["color"] = "Black"
print("Added Color:", phone["color"])

# 4. Deleting a key-value pair
del phone["is_5g"]  
print("After deleting is_5g:", phone)

phone = {
    "brand": "Apple",
    "model": "iPhone 15"
}

# 1. Using .get() for a key that exists
print(phone.get("model"))  # Output: iPhone 15

# 2. Using .get() for a key that DOES NOT exist
# Instead of crashing, it safely returns None
print(phone.get("price"))  # Output: None

# 3. Providing a custom default fallback value
# If the key isn't found, it returns your custom message
print(phone.get("price", "Price not listed"))  # Output: Price not listed
