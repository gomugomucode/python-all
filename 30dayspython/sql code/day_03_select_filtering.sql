-- ==========================================
-- DAY 3
-- SELECT, FILTERING, ORDER BY, LIMIT, OFFSET,
-- LIKE, NULL, DISTINCT, CASE
-- ==========================================

-- ==========================================
-- TASK 1 : EMPLOYEE QUERIES
-- ==========================================

-- 1. Return all employees
SELECT employee_id,
       full_name,
       job_title,
       salary,
       branch_id
FROM banking.employees;


-- 2. Highest salary to lowest
SELECT *
FROM banking.employees
ORDER BY salary DESC;


-- 3. Five highest-paid employees
SELECT *
FROM banking.employees
ORDER BY salary DESC
LIMIT 5;


-- 4. Salary between 40,000 and 80,000
SELECT *
FROM banking.employees
WHERE salary BETWEEN 40000 AND 80000;


-- 5. Job title is Loan Officer,
-- Branch Manager or Data Analyst
SELECT *
FROM banking.employees
WHERE job_title IN
('Loan Officer',
 'Branch Manager',
 'Data Analyst');


-- 6. Employee names start with S
SELECT *
FROM banking.employees
WHERE full_name LIKE 'S%';


-- 7. Names containing "ra"
-- regardless of capitalization
SELECT *
FROM banking.employees
WHERE full_name ILIKE '%ra%';


-- 8. Inactive employees
SELECT *
FROM banking.employees
WHERE is_active = FALSE;


-- 9. Unique job titles
SELECT DISTINCT job_title
FROM banking.employees;



-- ==========================================
-- TASK 2 : LOAN QUERIES
-- ==========================================

-- 1. Loans greater than 500000
SELECT *
FROM banking.loans
WHERE loan_amount > 500000;


-- 2. Loans started during 2025
SELECT *
FROM banking.loans
WHERE start_date BETWEEN
'2025-01-01'
AND
'2025-12-31';


-- 3. Loan status not CLOSED
SELECT *
FROM banking.loans
WHERE loan_status <> 'CLOSED';


-- 4. Sort by status then amount descending
SELECT *
FROM banking.loans
ORDER BY loan_status,
loan_amount DESC;


-- 5. First five loans
SELECT *
FROM banking.loans
LIMIT 5;


-- 6. Second page
-- (5 rows per page)

SELECT *
FROM banking.loans
LIMIT 5
OFFSET 5;


-- 7. Interest rate between 8 and 15
SELECT *
FROM banking.loans
WHERE interest_rate
BETWEEN 8 AND 15;


-- 8. Loan type HOME AUTO BUSINESS
SELECT *
FROM banking.loans
WHERE loan_type IN
('HOME',
 'AUTO',
 'BUSINESS');



-- ==========================================
-- TASK 3 : PAYMENT QUERIES
-- ==========================================

-- 1. Pending or failed payments
SELECT *
FROM banking.loan_payments
WHERE payment_status IN
('PENDING',
 'FAILED');


-- 2. Payments using ONLINE
SELECT *
FROM banking.loan_payments
WHERE payment_method = 'ONLINE';


-- 3. Payments between two dates
SELECT *
FROM banking.loan_payments
WHERE payment_date BETWEEN
'2025-05-01'
AND
'2025-08-31';


-- 4. Payment method is not null
SELECT *
FROM banking.loan_payments
WHERE payment_method IS NOT NULL;


-- 5. Largest five payments
SELECT *
FROM banking.loan_payments
ORDER BY payment_amount DESC
LIMIT 5;





-- ==========================================
-- TASK 4
-- Arithmetic and Aliases
-- ==========================================

SELECT
loan_id,
loan_amount,
interest_rate,

ROUND(
loan_amount * interest_rate / 100,
2
)
AS annual_interest_amount

FROM banking.loans;



-- ==========================================
-- TASK 5
-- CASE EXPRESSIONS
-- ==========================================

-- Employee salary classification

SELECT
employee_id,
full_name,
salary,

CASE

WHEN salary >=100000
THEN 'HIGH'

WHEN salary >=60000
THEN 'MEDIUM'

ELSE 'LOW'

END
AS salary_classification

FROM banking.employees;



-- Loan size classification

SELECT

loan_id,
loan_amount,

CASE

WHEN loan_amount >=1000000
THEN 'LARGE'

WHEN loan_amount >=300000
THEN 'MEDIUM'

ELSE 'SMALL'

END
AS loan_size

FROM banking.loans;



-- Payment status description

SELECT

payment_id,
payment_status,

CASE

WHEN payment_status='COMPLETED'
THEN 'Successful Payment'

WHEN payment_status='PENDING'
THEN 'Awaiting Confirmation'

WHEN payment_status='FAILED'
THEN 'Unsuccessful Payment'

END
AS payment_description

FROM banking.loan_payments;