-- ==========================================
-- DAY 4 : SQL JOINS
-- ==========================================


-- ==========================================
-- TASK 1 : INNER JOIN
-- Employees and Branches
-- ==========================================

SELECT
    e.full_name,
    e.job_title,
    e.salary,
    b.branch_name,
    b.city
FROM banking.employees AS e
INNER JOIN banking.branches AS b
ON e.branch_id = b.branch_id;


-- ==========================================
-- TASK 2 : LEFT JOIN
-- All branches and their employees
-- ==========================================

SELECT
    b.branch_id,
    b.branch_name,
    b.city,
    e.employee_id,
    e.full_name,
    e.job_title
FROM banking.branches AS b
LEFT JOIN banking.employees AS e
ON b.branch_id = e.branch_id
ORDER BY b.branch_id;


-- ==========================================
-- TASK 3 : Customer and Loan Report
-- ==========================================

SELECT
    c.customer_id,
    c.full_name,
    l.loan_id,
    l.loan_type,
    l.loan_amount,
    l.loan_status
FROM banking.customers AS c
LEFT JOIN banking.loans AS l
ON c.customer_id = l.customer_id
ORDER BY c.customer_id;


-- ==========================================
-- TASK 4 : RIGHT JOIN
-- Customers on the right side
-- ==========================================

SELECT
    c.customer_id,
    c.full_name,
    l.loan_id,
    l.loan_type,
    l.loan_amount,
    l.loan_status
FROM banking.loans AS l
RIGHT JOIN banking.customers AS c
ON l.customer_id = c.customer_id
ORDER BY c.customer_id;



-- ==========================================
-- TASK 5 : Loans and Payments
-- ==========================================

SELECT
    l.loan_id,
    l.loan_type,
    l.loan_amount,
    p.payment_id,
    p.payment_amount,
    p.payment_date,
    p.payment_status
FROM banking.loans AS l
LEFT JOIN banking.loan_payments AS p
ON l.loan_id = p.loan_id
ORDER BY l.loan_id;


-- ==========================================
-- TASK 6 : Join Four Tables
-- ==========================================

SELECT
    c.full_name,
    b.branch_name,
    l.loan_type,
    l.loan_amount,
    p.payment_amount,
    p.payment_date,
    p.payment_status
FROM banking.customers AS c
INNER JOIN banking.loans AS l
ON c.customer_id = l.customer_id
INNER JOIN banking.branches AS b
ON l.branch_id = b.branch_id
LEFT JOIN banking.loan_payments AS p
ON l.loan_id = p.loan_id
ORDER BY c.full_name;


-- ==========================================
-- TASK 7 : Missing Relationships
-- ==========================================

-- 1. Customers without loans

SELECT
    c.customer_id,
    c.full_name
FROM banking.customers AS c
LEFT JOIN banking.loans AS l
ON c.customer_id = l.customer_id
WHERE l.loan_id IS NULL;


-- 2. Loans without payments

SELECT
    l.loan_id,
    l.loan_type,
    l.loan_amount
FROM banking.loans AS l
LEFT JOIN banking.loan_payments AS p
ON l.loan_id = p.loan_id
WHERE p.payment_id IS NULL;


-- 3. Branches without employees

SELECT
    b.branch_id,
    b.branch_name
FROM banking.branches AS b
LEFT JOIN banking.employees AS e
ON b.branch_id = e.branch_id
WHERE e.employee_id IS NULL;


-- 4. Customers without accounts

SELECT
    c.customer_id,
    c.full_name
FROM banking.customers AS c
LEFT JOIN banking.accounts AS a
ON c.customer_id = a.customer_id
WHERE a.account_id IS NULL;


-- ==========================================
-- TASK 8 : FULL OUTER JOIN
-- ==========================================

CREATE TABLE banking.loan_targets
(
    loan_type VARCHAR(20),
    target_amount NUMERIC(14,2)
);


INSERT INTO banking.loan_targets
VALUES
('HOME',2500000),
('AUTO',1000000),
('EDUCATION',800000),
('GOLD',500000);


SELECT
    l.loan_type AS actual_loan_type,
    t.loan_type AS target_loan_type,
    t.target_amount
FROM
(
    SELECT DISTINCT loan_type
    FROM banking.loans
) AS l
FULL OUTER JOIN banking.loan_targets AS t
ON l.loan_type = t.loan_type;