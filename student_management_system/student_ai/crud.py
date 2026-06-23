from database import get_connection

def add_student(name, age, student_class, email):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO students(name, age, class, email)
        VALUES (%s,%s,%s,%s)
        """,
        (name, age, student_class, email)
    )

    conn.commit()

    cursor.close()
    conn.close()

    print("Student added successfully")


def get_students():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    cursor.close()
    conn.close()

    return students