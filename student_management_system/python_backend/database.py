
import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="student_ai",
        user="postgres",
        password="postgres123"
    )