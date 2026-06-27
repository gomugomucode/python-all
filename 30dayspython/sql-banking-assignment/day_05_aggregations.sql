-- ==========================================
-- DAY 5 : Aggregate Functions, GROUP BY, HAVING
-- ==========================================


-- ==========================================
-- TASK 1 : Basic Aggregates
-- ==========================================

-- 1. Total employees
SELECT COUNT(*) AS total_employees
FROM banking.employees;

-- 2. Total loans
SELECT COUNT(*) AS total_loans
FROM banking.loans;

-- 3. Total loan payments
SELECT COUNT(*) AS total_payments
FROM banking.loan_payments;

-- 4. Total loan amount
SELECT SUM(loan_amount) AS total_loan_amount
FROM banking.loans;

-- 5. Average loan amount
SELECT ROUND(AVG(loan_amount),2) AS average_loan_amount
FROM banking.loans;

-- 6. Minimum loan amount
SELECT MIN(loan_amount) AS minimum_loan_amount
FROM banking.loans;

-- 7. Maximum loan amount
SELECT MAX(loan_amount) AS maximum_loan_amount
FROM banking.loans;

-- 8. Average employee salary
SELECT ROUND(AVG(salary),2) AS average_salary
FROM banking.employees;

-- 9. Total completed payment amount
SELECT SUM(payment_amount) AS total_completed_payment
FROM banking.loan_payments
WHERE payment_status='COMPLETED';

-- 10. Earliest and latest loan start date
SELECT
MIN(start_date) AS earliest_start_date,
MAX(start_date) AS latest_start_date
FROM banking.loans;



-- ==========================================
-- TASK 2 : Group Employees
-- ==========================================

-- 1. Employee count by job title
SELECT
job_title,
COUNT(*) AS employee_count
FROM banking.employees
GROUP BY job_title;

-- 2. Employee count by branch
SELECT
branch_id,
COUNT(*) AS employee_count
FROM banking.employees
GROUP BY branch_id;

-- 3. Average salary by branch
SELECT
branch_id,
ROUND(AVG(salary),2) AS average_salary
FROM banking.employees
GROUP BY branch_id;

-- 4. Minimum and maximum salary by job title
SELECT
job_title,
MIN(salary) AS minimum_salary,
MAX(salary) AS maximum_salary
FROM banking.employees
GROUP BY job_title;



-- ==========================================
-- TASK 3 : Group Loans
-- ==========================================

SELECT
loan_type,
COUNT(*) AS loan_count,
SUM(loan_amount) AS total_loan_amount,
ROUND(AVG(loan_amount),2) AS average_loan_amount,
MIN(loan_amount) AS minimum_loan_amount,
MAX(loan_amount) AS maximum_loan_amount
FROM banking.loans
GROUP BY loan_type;



-- ==========================================
-- TASK 4 : Group by Multiple Columns
-- ==========================================

SELECT
branch_id,
job_title,
COUNT(*) AS employee_count,
ROUND(AVG(salary),2) AS average_salary
FROM banking.employees
GROUP BY
branch_id,
job_title
ORDER BY
branch_id,
job_title;



-- ==========================================
-- TASK 5 : Group Payments
-- ==========================================

SELECT
payment_status,
COUNT(*) AS payment_count,
SUM(payment_amount) AS total_payment_amount,
ROUND(AVG(payment_amount),2) AS average_payment_amount
FROM banking.loan_payments
GROUP BY payment_status;



-- ==========================================
-- TASK 6 : HAVING
-- ==========================================

-- 1. Loan types with total loan amount above 500000
SELECT
loan_type,
SUM(loan_amount) AS total_loan_amount
FROM banking.loans
GROUP BY loan_type
HAVING SUM(loan_amount) > 500000;


-- 2. Branches with at least two employees
SELECT
branch_id,
COUNT(*) AS employee_count
FROM banking.employees
GROUP BY branch_id
HAVING COUNT(*) >=2;


-- 3. Customers with total loan amount above 700000
SELECT
customer_id,
SUM(loan_amount) AS total_loan_amount
FROM banking.loans
GROUP BY customer_id
HAVING SUM(loan_amount) >700000;


-- 4. Loans with at least two payments
SELECT
loan_id,
COUNT(*) AS payment_count
FROM banking.loan_payments
GROUP BY loan_id
HAVING COUNT(*)>=2;


-- 5. Payment methods used at least three times
SELECT
payment_method,
COUNT(*) AS total_usage
FROM banking.loan_payments
GROUP BY payment_method
HAVING COUNT(*)>=3;



-- ==========================================
-- TASK 7 : WHERE and HAVING Together
-- ==========================================

SELECT
loan_type,
SUM(loan_amount) AS total_loan_amount,
ROUND(AVG(loan_amount),2) AS average_loan_amount
FROM banking.loans
WHERE start_date>='2025-01-01'
GROUP BY loan_type
HAVING COUNT(*)>=2;



-- ==========================================
-- TASK 8 : Branch Summary
-- ==========================================

SELECT
b.branch_id,
b.branch_name,

COALESCE(e.employee_count,0) AS employee_count,

COALESCE(l.loan_count,0) AS loan_count,

COALESCE(l.total_loan_amount,0) AS total_loan_amount,

COALESCE(l.average_loan_amount,0) AS average_loan_amount

FROM banking.branches AS b

LEFT JOIN
(
SELECT
branch_id,
COUNT(*) AS employee_count
FROM banking.employees
GROUP BY branch_id
) AS e
ON b.branch_id=e.branch_id

LEFT JOIN
(
SELECT
branch_id,
COUNT(*) AS loan_count,
SUM(loan_amount) AS total_loan_amount,
ROUND(AVG(loan_amount),2) AS average_loan_amount
FROM banking.loans
GROUP BY branch_id
) AS l
ON b.branch_id=l.branch_id

ORDER BY b.branch_id;