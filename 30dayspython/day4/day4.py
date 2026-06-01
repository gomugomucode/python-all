# 1. Storing data in correct data types
name = "Alex"                          # String
age = 28                               # Integer
height = 1.75                          # Float
is_student = True                      # Boolean
skills = ["Python", "Git", "SQL"]      # List
fav_languages = ("English", "Spanish") # Tuple
hobbies = {"Reading", "Cycling"}       # Set
personal_info = {                      # Dictionary
    "city": "New York", 
    "occupation": "Developer"
}

# 2. Printing the type of every variable
print("--- Variable Types ---")
print("name:", type(name))
print("age:", type(age))
print("height:", type(height))
print("is_student:", type(is_student))
print("skills:", type(skills))
print("fav_languages:", type(fav_languages))
print("hobbies:", type(hobbies))
print("personal_info:", type(personal_info))

# --- Extra Challenge ---
print("\n--- Extra Challenge Results ---")

# Task A: Add a new skill to the list
skills.append("Docker")
print("Updated skills list:", skills)

# Task B: Add duplicate values to the set
hobbies.add("Reading")
print("Set after trying to add duplicate 'Reading':", hobbies)

# Task C: Try modifying the tuple (This will cause an error, so we catch it)
try:
    fav_languages[0] = "French"
except TypeError as error:
    print("Tuple modification failed with error:", error)