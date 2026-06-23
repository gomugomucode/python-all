-- 1. Create the Database
CREATE DATABASE student_ai;

-- 2. Connect to the Database
\c student_ai

-- 3. Create Tables with Constraints
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT,
    class VARCHAR(20),
    email VARCHAR(100) UNIQUE NOT NULL  -- Added UNIQUE to prevent duplicate student emails
);

CREATE TABLE attendance (
    id SERIAL PRIMARY KEY,
    student_id INT REFERENCES students(id) ON DELETE CASCADE,
    attendance_percent FLOAT,
    CONSTRAINT unique_student_attendance UNIQUE (student_id) -- Prevents duplicate attendance entries
);

CREATE TABLE marks (
    id SERIAL PRIMARY KEY,
    student_id INT REFERENCES students(id) ON DELETE CASCADE,
    subject VARCHAR(50),
    marks INT,
    CONSTRAINT unique_student_subject UNIQUE (student_id, subject) -- Prevents duplicate marks for the same subject
);

-- 4. Insert Data
INSERT INTO students(name, age, class, email)
VALUES
('Anupam', 20, 'BCA', 'anupam@gmail.com'),
('Ram', 21, 'BCA', 'ram@gmail.com'),
('Hari', 19, 'BCA', 'hari@gmail.com');

INSERT INTO attendance(student_id, attendance_percent)
VALUES
(1, 92),
(2, 78),
(3, 85);

INSERT INTO marks(student_id, subject, marks)
VALUES
(1, 'Python', 95),
(2, 'Python', 75),
(3, 'Python', 88);
