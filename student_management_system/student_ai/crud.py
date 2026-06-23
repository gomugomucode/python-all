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

def update_attendance(student_id, new_attendance_percent):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE attendance
        SET attendance_percent = %s
        WHERE student_id = %s
        """,
        (new_attendance_percent, student_id)
    )

    conn.commit()

    cursor.close()
    conn.close()

    print("Attendance updated successfully")

def add_marks(student_id, subject, marks):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO marks(student_id, subject, marks)
        VALUES (%s,%s,%s)
        """,
        (student_id, subject, marks)
    )

    conn.commit()

    cursor.close()
    conn.close()

    print("Marks added successfully")

def get_marks(student_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM marks
        WHERE student_id = %s
        """,
        (student_id,)
    )

    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result

def update_marks(student_id, subject, new_marks):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE marks
        SET marks = %s
        WHERE student_id = %s
        AND subject = %s
        """,
        (new_marks, student_id, subject)
    )

    conn.commit()

    cursor.close()
    conn.close()

    print("Marks updated successfully")

def students_above_marks(min_marks):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT s.name,
               m.subject,
               m.marks
        FROM students s
        JOIN marks m
        ON s.id = m.student_id
        WHERE m.marks > %s
        """,
        (min_marks,)
    )

    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result

def highest_attendance():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT s.name,
               a.attendance_percent
        FROM students s
        JOIN attendance a
        ON s.id = a.student_id
        ORDER BY a.attendance_percent DESC
        LIMIT 1
        """
    )

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result