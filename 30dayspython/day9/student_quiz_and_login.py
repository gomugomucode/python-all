# Student Login & Quiz System

# 1. Password Verification System
correct_password = "python123"
attempts = 3
login_success = False

print("--- Welcome to the Student Quiz System ---")

while attempts > 0:
    password_input = input(f"Enter password ({attempts} attempts left): ")
    
    if password_input == correct_password:
        print("\nLogin successful! Welcome to the quiz.")
        login_success = True
        break
    else:
        attempts -= 1
        if attempts > 0:
            print("Incorrect password. Try again.")
        else:
            print("\nToo many incorrect attempts. System locked.")

# 2. Quiz System (Only runs if login succeeded)
if login_success:
    # Quiz questions and answers stored as tuples (Question, Answer)
    questions = [
        ("What is the keyword to define a function in Python?", "def"),
        ("Which loop is used for a known number of iterations?", "for"),
        ("What data type holds True or False?", "boolean"),
        ("Which keyword skips the current iteration of a loop?", "continue")
    ]
    
    score = 0
    print("\n--- Quiz Started ---")
    print("Type 'exit' to quit the quiz at any time.")
    print("Leave the answer blank and press Enter to skip a question.\n")
    
    for question, correct_answer in questions:
        # Pass used as a placeholder for a future feature (e.g., tracking question timers)
        pass 
        
        user_answer = input(f"{question}: ").strip().lower()
        
        # Check for exit condition
        if user_answer == "exit":
            print("\nYou chose to exit the quiz early.")
            break
            
        # Check for skipped question
        if user_answer == "":
            print("Question skipped.\n")
            continue
            
        # Validate the answer
        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {correct_answer}\n")
            
    # 3. Final Score & Percentage Display
    print("--- Quiz Results ---")
    print(f"Your final score: {score}/{len(questions)}")
    
    # Calculate the percentage
    percentage = (score / len(questions)) * 100
    print(f"Percentage: {percentage:.1f}%")
    
    # Provide grade feedback using conditions
    if percentage >= 80:
        print("Performance: Excellent work!")
    elif percentage >= 50:
        print("Performance: Good job, but room for improvement.")
    else:
        print("Performance: Needs study. Try reviewing the modules.")
