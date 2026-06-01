import csv
import datetime
import os

# Define the file name where Excel-compatible data is stored
FILE_NAME = "student_records.csv"

# Ensure the CSV file exists and has headers if it's being created for the first time
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Name", "Age", "Skills", "Average Marks", "Status"])

def add_student():
    """Prompts for student details, processes metrics, and writes to CSV."""
    print("\n--- Enter New Student Details ---")
    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty!")
        return

    try:
        age = int(input(f"Enter age for {name}: "))
    except ValueError:
        print("Invalid age. Defaulting to 0.")
        age = 0

    skills_input = input("Enter skills separated by commas: ")
    # Clean up whitespace and filter out empty elements
    skills_list = [s.strip() for s in skills_input.split(",") if s.strip()]
    skills_string = ", ".join(skills_list) if skills_list else "None"

    # Dynamic input loop for subjects and grades
    marks = {}
    print("\n--- Enter Subject Marks (Press Enter on empty subject to finish) ---")
    while True:
        subject = input("Enter subject name: ").strip()
        if not subject:
            break
        try:
            grade = float(input(f"Enter mark for {subject}: "))
            marks[subject] = grade
        except ValueError:
            print("Invalid grade format. Please enter a valid number.")

    # Process final metrics
    if marks:
        total_marks = sum(marks.values())
        average_marks = round(total_marks / len(marks), 1)
        
        # Passing rule: average >= 50 and no individual grade below 40
        has_good_average = average_marks >= 50
        passed_all_subjects = all(grade >= 40 for grade in marks.values())
        status = "Passed" if (has_good_average and passed_all_subjects) else "Failed"
    else:
        average_marks = 0.0
        status = "No Marks Entered"

    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Append row to CSV file
    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, name, age, skills_string, average_marks, status])
        
    print(f"\n✔️ Profile for {name} saved successfully to '{FILE_NAME}'.")

def view_records():
    """Reads the CSV file and prints all student rows in a formatted layout."""
    if not os.path.exists(FILE_NAME):
        print("\nNo records file found yet. Add a student first!")
        return

    print("\n==================== PAST STUDENT RECORDS ====================")
    # Using format specifiers to align the output column text perfectly
    print(f"{'Date & Time':<21} | {'Name':<12} | {'Age':<4} | {'Average':<7} | {'Status':<8} | {'Skills'}")
    print("-" * 80)

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row so it doesn't print twice
        
        row_count = 0
        for row in reader:
            if not row:  # Skip empty lines if any exist
                continue
            timestamp, name, age, skills, avg_marks, status = row
            print(f"{timestamp:<21} | {name:<12} | {age:<4} | {avg_marks:<7} | {status:<8} | {skills}")
            row_count += 1
            
    if row_count == 0:
        print("The database file is currently empty.")
    print("==============================================================")

# Main System Interface Loop
while True:
    print("\n===== Student Database Menu =====")
    print("1. Add New Student Profile")
    print("2. View All Past Records")
    print("3. Exit System")
    
    choice = input("Select an option (1-3): ").strip()
    
    if choice == "1":
        add_student()
    elif choice == "2":
        view_records()
    elif choice == "3":
        print("Exiting system. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
