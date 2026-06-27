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

