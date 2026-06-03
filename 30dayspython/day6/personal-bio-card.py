# Personal Bio-Data Card

# String inputs
full_name = input("Enter your full name: ")
city = input("Enter your city: ")

# Integer and Float inputs
age = int(input("Enter your age: "))
height = float(input("Enter your height (in meters): "))

# Boolean input
student_input = input("Are you a student? (yes/no): ").lower()
is_student = student_input == "yes"

# Tuple for birth date
day = int(input("Enter birth day: "))
month = int(input("Enter birth month: "))
year = int(input("Enter birth year: "))
birth_date = (day, month, year)

# List for hobbies
hobbies = []
print("\nEnter 3 hobbies:")
for i in range(3):
    hobby = input(f"Hobby {i+1}: ")
    hobbies.append(hobby)

# Set for languages
languages = set()
print("\nEnter 3 languages:")
for i in range(3):
    language = input(f"Language {i+1}: ")
    languages.add(language)

# Dictionary for complete profile
profile = {
    "Name": full_name,
    "City": city,
    "Age": age,
    "Height": height,
    "Student": is_student,
    "Birth Date": birth_date,
    "Hobbies": hobbies,
    "Languages": languages
}

# Formatted Bio-Data Card
print("\n" + "=" * 50)
print("              PERSONAL BIO-DATA CARD")
print("=" * 50)

print(f"Name              : {profile['Name']}")
print(f"City              : {profile['City']}")
print(f"Age               : {profile['Age']}")
print(f"Height            : {profile['Height']} m")
print(f"Student           : {profile['Student']}")
print(f"Birth Date        : {profile['Birth Date']}")
print(f"Hobbies           : {profile['Hobbies']}")
print(f"Languages         : {profile['Languages']}")

print("-" * 50)

# String indexing
print(f"First Letter Name : {full_name[0]}")

# Length checks
print(f"Number of Hobbies : {len(hobbies)}")
print(f"Unique Languages  : {len(languages)}")

print("-" * 50)

# Display data types
print(f"Type of Name      : {type(full_name)}")
print(f"Type of Age       : {type(age)}")
print(f"Type of Height    : {type(height)}")
print(f"Type of Student   : {type(is_student)}")
print(f"Type of BirthDate : {type(birth_date)}")
print(f"Type of Hobbies   : {type(hobbies)}")
print(f"Type of Languages : {type(languages)}")

print("=" * 50)