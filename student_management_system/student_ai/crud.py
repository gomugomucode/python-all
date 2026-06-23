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


def update_student_email(student_id, new_email):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE students
        SET email = %s
        WHERE id = %s
        """,
        (new_email, student_id)
    )

    conn.commit()

    cursor.close()
    conn.close()

    print("Student updated successfully")


def delete_student(student_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM students
        WHERE id = %s
        """,
        (student_id,)
    )

    conn.commit()

    cursor.close()
    conn.close()

    print("Student deleted successfully")