# student Marks Management System

name  = input("Enter your name: ")
print("Hello " + name)

n = int(input("Enter the number of subjects: "))
subjects = []
for i in range(n):
    subject = input("Enter subject " + str(i+1) + ": ")
    subjects.append(subject)

print("Subjects:", subjects)

marks = []
for i in range(n):
    mark = int(input("Enter marks for " + subjects[i] + ": "))
    marks.append(mark)

print("Marks:", marks)

total_marks = sum(marks)
print("Total Marks:", total_marks)

average_marks = total_marks / n
print("Average Marks:", average_marks)

highest_mark = max(marks)
print("Highest Mark:", highest_mark)

lowest_mark = min(marks)
print("Lowest Mark:", lowest_mark)


