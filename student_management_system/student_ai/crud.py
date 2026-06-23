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

def search_student(name):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM students
        WHERE name ILIKE %s
        """,
        (f"%{name}%",)
    )

    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result

def add_attendance(student_id, attendance_percent):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO attendance(student_id, attendance_percent)
        VALUES (%s,%s)
        """,
        (student_id, attendance_percent)
    )

    conn.commit()

    cursor.close()
    conn.close()

    print("Attendance added successfully")

def get_attendance(student_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM attendance
        WHERE student_id = %s
        """,
        (student_id,)
    )

    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result

