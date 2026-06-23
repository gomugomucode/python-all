# from crud import add_student

# add_student(
#     "Sita",
#     20,
#     "BCA",
#     "sita@gmail.com"
# )

from crud import get_students

students = get_students()

for student in students:
    print(student)