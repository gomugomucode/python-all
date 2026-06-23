# from crud import add_student

# add_student(
#     "Sita",
#     20,
#     "BCA",
#     "sita@gmail.com"
# )

# from crud import get_students

# students = get_students()

# for student in students:
#     print(student)

# from crud import update_student_email

# update_student_email(
#     1,
#     "anupam_new@gmail.com"
# )

# from crud import delete_student

# delete_student(4)


from crud import search_student

students = search_student("anu")

for student in students:
    print(student)