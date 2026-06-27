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


