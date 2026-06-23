def add_student(name, age, student_class, email):

    cursor.execute(
        """
        INSERT INTO students(name, age, class, email)
        VALUES(%s,%s,%s,%s)
        """,
        (name, age, student_class, email)
    )

    conn.commit()