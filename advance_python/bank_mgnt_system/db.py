import sqlite3

conn = sqlite3.connect("bank_mgmt_system.db")
cursor = conn.cursor()

# Notice the 'S' in EXISTS and the parentheses instead of curly braces.
sql_command = """ 
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    account_number INTEGER NOT NULL UNIQUE,
    balance INTEGER NOT NULL
)
"""

cursor.execute(sql_command)
conn.commit()
conn.close()

print("Database and table created successfully.")