# Task 1 created the letter_grade(score)
def letter_grade(score):
    if score < 0 or score > 100:
        raise ValueError(f"Invalid score: {score}. Score must be between 0 and 100.")
        
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
         