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


