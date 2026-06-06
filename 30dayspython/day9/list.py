# # student Marks Management System

# name  = input("Enter your name: ")
# print("Hello " + name)

# n = int(input("Enter the number of subjects: "))
# subjects = []
# for i in range(n):
#     subject = input("Enter subject " + str(i+1) + ": ")
#     subjects.append(subject)

# print("Subjects:", subjects)

# marks = []
# for i in range(n):
#     mark = int(input("Enter marks for " + subjects[i] + ": "))
#     marks.append(mark)

# print("Marks:", marks)

# total_marks = sum(marks)
# print("Total Marks:", total_marks)

# average_marks = total_marks / n
# print("Average Marks:", average_marks)

# highest_mark = max(marks)
# print("Highest Mark:", highest_mark)

# lowest_mark = min(marks)
# print("Lowest Mark:", lowest_mark)



my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)

my_list.append(6)
print("After Append:", my_list)

my_list.insert(2, 10)
print("After Insert:", my_list)

my_list.remove(3)
print("After Remove:", my_list)

my_list.pop()
print("After Pop:", my_list)

my_list.sort()
print("After Sort:", my_list)

my_list.reverse()
print("After Reverse:", my_list)


