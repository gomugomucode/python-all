import sqlite3

# 1. Connect to a database file (it creates it if it doesn't exist)
connection = sqlite3.connect('school.db')
cursor = connection.cursor()

# 2. Create the table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        grade REAL
    )
''')

# 3. Insert some data
cursor.execute("INSERT INTO students (name, grade) VALUES ('Charlie', 88.0)")

# 4. Save (Commit) the changes
connection.commit()

# 5. Read the data back

# cursor.execute("SELECT * FROM students")
# rows = cursor.fetchall()
# for row in rows:
#     print(f"ID: {row[0]}, Name: {row[1]}, Grade: {row[2]}")


min_grade = 80.0

# ?this mean the mingrade is tuple bcuz after min grade the comma is used which mean there are other number also 
cursor.execute("SELECT * FROM students WHERE grade > ?", (min_grade,))

# in thsi the min grade is see ans the list  bcuz of the bracket and no traling comma 
cursor.execute("SELECT * FROM students WHERE grade > ?", [min_grade]) # No comma needed!
result = cursor.fetchall()
print(result)




# 6. Close the connection
connection.close()