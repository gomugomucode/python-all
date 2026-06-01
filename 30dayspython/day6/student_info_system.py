# --- 1. Variables and Data Types (Taking User Inputs) ---
student_name = input("Enter student name: ").strip()

# Using try/except blocks to prevent crashes if the user types letters for numbers
try:
    student_age = int(input("Enter student age: "))
except ValueError:
    print("Invalid age entered. Defaulting to 0.")
    student_age = 0

# Taking skills as a comma-separated string and converting it into a list
skills_input = input("Enter skills separated by commas (e.g., Python, React): ")
student_skills = [skill.strip() for skill in skills_input.split(",") if skill.strip()]

# Dictionary storing individual subject scores from user input
print("\n--- Enter Subject Marks ---")
try:
    math_mark = float(input("Enter Math mark: "))
    science_mark = float(input("Enter Science mark: "))
    english_mark = float(input("Enter English mark: "))
except ValueError:
    print("Invalid mark entered. Defaulting to 0 for missing values.")
    math_mark = math_mark if 'math_mark' in locals() else 0.0
    science_mark = science_mark if 'science_mark' in locals() else 0.0
    english_mark = english_mark if 'english_mark' in locals() else 0.0

marks = {
    "Math": math_mark,
    "Science": science_mark,
    "English": english_mark
}

# --- 2. Arithmetic Operators (Calculating Average Marks) ---
total_marks = marks["Math"] + marks["Science"] + marks["English"]
number_of_subjects = len(marks)
average_marks = total_marks / number_of_subjects  # Float result

# --- 3. Comparison & Logical Operators (Determining Status) ---
# Rules: Must have an average >= 50 AND no individual subject score below 40
has_good_average = average_marks >= 50
passed_all_subjects = (marks["Math"] >= 40) and (marks["Science"] >= 40) and (marks["English"] >= 40)

# Logical 'and' to determine final status
is_passed = has_good_average and passed_all_subjects  # Boolean

# Convert boolean status to a clean display string
status_text = "Passed" if is_passed else "Failed"

# --- 4. Displaying the Profile ---
print("\n===== Student Profile =====")
print(f"Name: {student_name}")
print(f"Age: {student_age}")

# Joining list elements into a single comma-separated string
skills_string = ", ".join(student_skills) if student_skills else "None"
print(f"Skills: {skills_string}")
print()  # Empty line for formatting
print(f"Average Marks: {average_marks:.1f}")
print(f"Status: {status_text}")
