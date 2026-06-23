CREATE DATABASE student_ai;

\c student_ai

CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    class VARCHAR(20),
    email VARCHAR(100)
);

CREATE TABLE attendance (
    id SERIAL PRIMARY KEY,
    student_id INT REFERENCES students(id),
    attendance_percent FLOAT
);

CREATE TABLE marks (
    id SERIAL PRIMARY KEY,
    student_id INT REFERENCES students(id),
    subject VARCHAR(50),
    marks INT
);

INSERT INTO students(name,age,class,email)
VALUES
('Anupam',20,'BCA','anupam@gmail.com'),
('Ram',21,'BCA','ram@gmail.com'),
('Hari',19,'BCA','hari@gmail.com');

INSERT INTO attendance(student_id,attendance_percent)
VALUES
(1,92),
(2,78),
(3,85);

INSERT INTO marks(student_id,subject,marks)
VALUES
(1,'Python',95),
(2,'Python',75),
(3,'Python',88);