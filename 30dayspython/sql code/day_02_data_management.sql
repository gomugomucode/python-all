-- ==========================================
-- DAY 2: DATA INSERTION AND MODIFICATION
-- ==========================================

-- ==========================================
-- Task 1: Insert Employees
-- ==========================================

INSERT INTO banking.employees
(employee_id, branch_id, full_name, email, job_title, salary, hire_date, is_active)
VALUES
(1, 1, 'Anupam Baral', '[anupam@bank.com](mailto:anupam@bank.com)', 'Data Analyst', 65000, '2024-01-15', TRUE),
(2, 1, 'Ram Sharma', '[ram@bank.com](mailto:ram@bank.com)', 'Loan Officer', 55000, '2024-02-10', TRUE),
(3, 2, 'Sita Karki', '[sita@bank.com](mailto:sita@bank.com)', 'Branch Manager', 120000, '2023-06-12', TRUE),
(4, 2, 'Hari Thapa', '[hari@bank.com](mailto:hari@bank.com)', 'Customer Service Officer', 45000, '2024-03-01', TRUE),
(5, 3, 'Gita Rai', '[gita@bank.com](mailto:gita@bank.com)', 'Accountant', 70000, '2023-11-05', TRUE),
(6, 3, 'Nabin Gautam', '[nabin@bank.com](mailto:nabin@bank.com)', 'Loan Officer', 60000, '2024-04-10', FALSE),
(7, 1, 'Sarita KC', '[sarita@bank.com](mailto:sarita@bank.com)', 'Customer Service Officer', 50000, '2024-05-15', TRUE),
(8, 2, 'Prakash Bista', '[prakash@bank.com](mailto:prakash@bank.com)', 'Data Analyst', 75000, '2024-01-20', TRUE);

-- Branch 4 intentionally has no employees

-- ==========================================
-- Task 2: Insert Loans
-- ==========================================

INSERT INTO banking.loans
(loan_id, customer_id, branch_id, loan_type, loan_amount,
interest_rate, start_date, end_date, loan_status)
VALUES
(101, 1, 1, 'HOME', 1500000, 10.5, '2025-01-01', '2035-01-01', 'ACTIVE'),
(102, 1, 1, 'AUTO', 500000, 9.5, '2025-02-01', '2030-02-01', 'ACTIVE'),

(103, 2, 2, 'PERSONAL', 250000, 12.0, '2025-03-01', '2028-03-01', 'CLOSED'),
(104, 2, 2, 'BUSINESS', 2000000, 11.0, '2025-04-01', '2035-04-01', 'ACTIVE'),

(105, 3, 3, 'AUTO', 450000, 8.5, '2025-05-01', '2030-05-01', 'DEFAULTED'),
(106, 4, 1, 'HOME', 1800000, 10.0, '2025-06-01', '2035-06-01', 'ACTIVE'),
(107, 5, 2, 'PERSONAL', 300000, 13.0, '2025-07-01', '2028-07-01', 'ACTIVE'),
(108, 6, 3, 'BUSINESS', 2500000, 12.5, '2025-08-01', '2035-08-01', 'ACTIVE');

-- Customer 7 intentionally has no loan
-- Loan 108 intentionally has no payment

-- ==========================================
-- Task 3: Insert Loan Payments
-- ==========================================

INSERT INTO banking.loan_payments
(payment_id, loan_id, payment_amount, payment_date,
payment_method, payment_status)
VALUES
(1,101,50000,'2025-02-01','ONLINE','COMPLETED'),
(2,101,50000,'2025-03-01','ONLINE','COMPLETED'),
(3,101,50000,'2025-04-01','BANK_TRANSFER','COMPLETED'),

(4,102,25000,'2025-03-10','CASH','COMPLETED'),
(5,102,25000,'2025-04-10','CHEQUE','COMPLETED'),

(6,103,30000,'2025-05-01','ONLINE','COMPLETED'),
(7,103,30000,'2025-06-01','BANK_TRANSFER','COMPLETED'),

(8,104,60000,'2025-05-15','ONLINE','PENDING'),
(9,104,60000,'2025-06-15','ONLINE','COMPLETED'),

(10,105,20000,'2025-06-10','CHEQUE','FAILED'),
(11,105,25000,'2025-07-10','CASH','COMPLETED'),

(12,106,70000,'2025-08-01','BANK_TRANSFER','COMPLETED'),
(13,106,70000,'2025-09-01','ONLINE','COMPLETED'),

(14,107,15000,'2025-08-15','CASH','COMPLETED'),
(15,107,15000,'2025-09-15','CHEQUE','COMPLETED');

-- ==========================================
-- Task 4: ALTER TABLE
-- ==========================================

ALTER TABLE banking.employees
ADD COLUMN phone_number VARCHAR(15);

ALTER TABLE banking.employees
RENAME COLUMN phone_number TO contact_number;

ALTER TABLE banking.employees
ALTER COLUMN contact_number TYPE VARCHAR(25);

CREATE TABLE banking.loan_notes_temp (
note_id INT PRIMARY KEY,
note_text VARCHAR(255)
);

ALTER TABLE banking.loan_notes_temp
ADD COLUMN created_at TIMESTAMP;

ALTER TABLE banking.loan_notes_temp
ADD COLUMN created_by VARCHAR(100);

DROP TABLE banking.loan_notes_temp;

-- ==========================================
-- Task 5: UPDATE
-- ==========================================

-- Increase salary by 10%

SELECT *
FROM banking.employees
WHERE employee_id = 1;

UPDATE banking.employees
SET salary = salary * 1.10
WHERE employee_id = 1;

-- Mark employee inactive

SELECT *
FROM banking.employees
WHERE employee_id = 2;

UPDATE banking.employees
SET is_active = FALSE
WHERE employee_id = 2;

-- Change active loan to closed

SELECT *
FROM banking.loans
WHERE loan_id = 101;

UPDATE banking.loans
SET loan_status = 'CLOSED'
WHERE loan_id = 101;

-- Change pending payment to completed

SELECT *
FROM banking.loan_payments
WHERE payment_id = 8;

UPDATE banking.loan_payments
SET payment_status = 'COMPLETED'
WHERE payment_id = 8;

-- ==========================================
-- Task 6: DELETE
-- ==========================================

INSERT INTO banking.loan_payments
(payment_id, loan_id, payment_amount, payment_date,
payment_method, payment_status)
VALUES
(99,101,1000,'2025-12-01','CASH','PENDING');

SELECT *
FROM banking.loan_payments
WHERE payment_id = 99;

DELETE FROM banking.loan_payments
WHERE payment_id = 99;

SELECT *
FROM banking.loan_payments
WHERE payment_id = 99;


