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
         
# Task 2 created the analyse(students)
def analyse(students):
    analyzed_data = {}
    for  name , score in students.items():
        grade = letter_grade(score)
        analyzed_data[name] = {"score" : score , "grade":grade }
    return analyzed_data
    
# Task 3 created the summary(results)
def summary(results):
    # Print individual student grades cleanly
    for name, data in results.items():
        print(f"{name:<7}: {data['score']} → {data['grade']}")
    print() 

    # Calculate average score
    scores = [data["score"] for data in results.values()]
    average = sum(scores) / len(scores)
    print(f"Class Average : {average:.2f}")
# this code is the simple version  of above without list comprehension
  #  # 2. Calculate average (Standard Loop)
    # total_score = 0
    # for data in results.values():
    #     total_score += data["score"]
    # average = total_score / len(results)
    # print(f"Class Average : {average:.2f}")



    # Find highest and lowest scorers using max/min
    highest_name = max(results, key=lambda k: results[k]["score"])
    lowest_name = min(results, key=lambda k: results[k]["score"])
    
    print(f"Highest Score : {highest_name} ({results[highest_name]['score']})")
    print(f"Lowest Score  : {lowest_name} ({results[lowest_name]['score']})")

  
    # # --- HERE IS THE SIMPLIFIED MIN/MAX --- without lambda, using an inner function instead
    # # Inner function that tells max() how to read the score
    # def get_score(name):
    #     return results[name]["score"]

    # highest_name = max(results, key=get_score)
    # lowest_name = min(results, key=get_score)
    # # --------------------------------------

    # print(f"Highest Score : {highest_name} ({results[highest_name]['score']})")
    # print(f"Lowest Score  : {lowest_name} ({results[lowest_name]['score']})")


    # Count grade distributions using sorted order
    counts = {}
    for data in results.values():
        grade = data["grade"]
        # [ Where to save ]   [ Look up existing ]   [ Add ]
        counts[grade]   =   counts.get(grade, 0)   +   1

# this code is the same as above 1 line code of 71 but without using get() method
#         if grade not in counts:
        #     counts[grade] = 0  # Create it first if missing
        # counts[grade] = counts[grade] + 1  # Then add 1


    # Format the counts summary line dynamically
    grade_order = ["A", "B", "C", "D", "F"]
    count_strings = [f"{g}={counts.get(g, 0)}" for g in grade_order]
    print(f"Grade Counts  : {'  '.join(count_strings)}")

# Task 4: Wrap execution in try/except and test valid + invalid inputs
if __name__ == "__main__":
    # Test Case 1: Valid Sample Input
    print("--- Test Case 1: Valid Input ---")
    try:
        students = {
            "Alice": 92, "Bob": 78, "Carol": 85,
            "Dave": 61, "Eve": 55, "Frank": 99
        }
        analyzed_results = analyse(students)
        summary(analyzed_results)
    except ValueError as e:
        print(f"Error caught: {e}")

    print("\n--- Test Case 2: Invalid Input ---")
    # Test Case 2: Triggering the error using Task 4 requirements
    try:
        invalid_students = {"Alice": 92, "BadStudent": 110}
        analyzed_results = analyse(invalid_students)
        summary(analyzed_results)
    except ValueError as e:
        print(f"Error caught: {e}")