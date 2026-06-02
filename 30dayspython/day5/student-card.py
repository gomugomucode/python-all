# Student Report Card Generator

# Input student details
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

# Input marks
subject1 = float(input("Enter marks in Subject 1: "))
subject2 = float(input("Enter marks in Subject 2: "))
subject3 = float(input("Enter marks in Subject 3: "))

# Store data in a dictionary
student = {
    "Name": name,
    "Roll Number": roll_no,
    "Subject 1": subject1,
    "Subject 2": subject2,
    "Subject 3": subject3
}

# Calculate total and percentage
total = subject1 + subject2 + subject3
percentage = total / 3

# Pass/Fail using logical operators
is_pass = (subject1 >= 40 and
           subject2 >= 40 and
           subject3 >= 40)

# Grade assignment
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

# Distinction using nested if and set membership
remark = "No Distinction"

if is_pass:
    if grade in {"A+", "A"}:
        remark = "Distinction"

# Final status using ternary operator
status = "PASS" if is_pass else "FAIL"

# Report Card Output
print("\n" + "=" * 40)
print("         STUDENT REPORT CARD")
print("=" * 40)

print(f"Name        : {student['Name']}")
print(f"Roll Number : {student['Roll Number']}")

print("-" * 40)
print(f"Subject 1   : {subject1}")
print(f"Subject 2   : {subject2}")
print(f"Subject 3   : {subject3}")
print("-" * 40)

print(f"Total Marks : {total}")
print(f"Percentage  : {percentage:.2f}%")
print(f"Grade       : {grade}")
print(f"Remark      : {remark}")
print(f"Status      : {status}")

print("=" * 40)