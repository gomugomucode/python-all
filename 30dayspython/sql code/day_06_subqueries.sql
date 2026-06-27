-- ==========================================
-- DAY 6 : SUBQUERIES & NESTED QUERIES
-- ==========================================

-- ==========================================
-- TASK 1 : Scalar Subqueries
-- ==========================================

-- 1. Loans greater than the average loan amount
SELECT *
FROM banking.loans
WHERE loan_amount >
(
    SELECT AVG(loan_amount)
    FROM banking.loans
);

-- 2. Employees earning above the average salary
SELECT *
FROM banking.employees
WHERE salary >
(
    SELECT AVG(salary)
    FROM banking.employees
);

-- 3. Payments greater than the average payment amount
SELECT *
FROM banking.loan_payments
WHERE payment_amount >
(
    SELECT AVG(payment_amount)
    FROM banking.loan_payments
);

-- 4. Loans with interest rate greater than average interest rate
SELECT *
FROM banking.loans
WHERE interest_rate >
(
    SELECT AVG(interest_rate)
    FROM banking.loans
);


-- ==========================================
-- TASK 2 : IN with Subquery
-- ==========================================

-- 1. Customers who have a HOME loan
SELECT *
FROM banking.customers
WHERE customer_id IN
(
    SELECT customer_id
    FROM banking.loans
    WHERE loan_type = 'HOME'
);

-- 2. Customers who have an ACTIVE loan
SELECT *
FROM banking.customers
WHERE customer_id IN
(
    SELECT customer_id
    FROM banking.loans
    WHERE loan_status = 'ACTIVE'
);

-- 3. Branches that issued an AUTO loan
SELECT *
FROM banking.branches
WHERE branch_id IN
(
    SELECT branch_id
    FROM banking.loans
    WHERE loan_type = 'AUTO'
);

-- 4. Employees working in branches that have ACTIVE loans
SELECT *
FROM banking.employees
WHERE branch_id IN
(
    SELECT branch_id
    FROM banking.loans
    WHERE loan_status = 'ACTIVE'
);


-- ==========================================
-- TASK 3 : Subquery in HAVING
-- ==========================================

-- 1. Loan types with average loan amount greater
-- than overall average loan amount

SELECT
loan_type,
AVG(loan_amount) AS average_loan
FROM banking.loans
GROUP BY loan_type
HAVING AVG(loan_amount) >
(
    SELECT AVG(loan_amount)
    FROM banking.loans
);

-- 2. Branches whose average employee salary
-- is greater than overall average salary

SELECT
branch_id,
AVG(salary) AS average_salary
FROM banking.employees
GROUP BY branch_id
HAVING AVG(salary) >
(
    SELECT AVG(salary)
    FROM banking.employees
);


-- ==========================================
-- TASK 4 : Subquery in FROM (Inline View)
-- ==========================================

SELECT
p.loan_id,
p.payment_count,
p.total_completed_payment,
p.average_completed_payment
FROM
(
    SELECT
    loan_id,
    COUNT(*) AS payment_count,
    SUM(payment_amount) AS total_completed_payment,
    ROUND(AVG(payment_amount),2) AS average_completed_payment

    FROM banking.loan_payments

    WHERE payment_status='COMPLETED'

    GROUP BY loan_id
) AS p

WHERE p.payment_count >=2;


-- ==========================================
-- TASK 5 : EXISTS
-- ==========================================

-- 1. Customers with at least one loan

SELECT *
FROM banking.customers c
WHERE EXISTS
(
    SELECT 1
    FROM banking.loans l
    WHERE l.customer_id=c.customer_id
);

-- 2. Loans with at least one completed payment

SELECT *
FROM banking.loans l
WHERE EXISTS
(
    SELECT 1
    FROM banking.loan_payments p
    WHERE p.loan_id=l.loan_id
    AND p.payment_status='COMPLETED'
);

-- 3. Branches with at least one employee

SELECT *
FROM banking.branches b
WHERE EXISTS
(
    SELECT 1
    FROM banking.employees e
    WHERE e.branch_id=b.branch_id
);

-- 4. Customers having both account and loan

SELECT *
FROM banking.customers c

WHERE EXISTS
(
    SELECT 1
    FROM banking.accounts a
    WHERE a.customer_id=c.customer_id
)

AND EXISTS
(
    SELECT 1
    FROM banking.loans l
    WHERE l.customer_id=c.customer_id
);


-- ==========================================
-- TASK 6 : NOT EXISTS
-- ==========================================

-- 1. Customers without loans

SELECT *
FROM banking.customers c
WHERE NOT EXISTS
(
    SELECT 1
    FROM banking.loans l
    WHERE l.customer_id=c.customer_id
);

-- 2. Loans without payments

SELECT *
FROM banking.loans l
WHERE NOT EXISTS
(
    SELECT 1
    FROM banking.loan_payments p
    WHERE p.loan_id=l.loan_id
);

-- 3. Loans without completed payments

SELECT *
FROM banking.loans l
WHERE NOT EXISTS
(
    SELECT 1
    FROM banking.loan_payments p
    WHERE p.loan_id=l.loan_id
    AND p.payment_status='COMPLETED'
);

-- 4. Branches without employees

SELECT *
FROM banking.branches b
WHERE NOT EXISTS
(
    SELECT 1
    FROM banking.employees e
    WHERE e.branch_id=b.branch_id
);

-- 5. Customers having accounts but no loans

SELECT *
FROM banking.customers c

WHERE EXISTS
(
    SELECT 1
    FROM banking.accounts a
    WHERE a.customer_id=c.customer_id
)

AND NOT EXISTS
(
    SELECT 1
    FROM banking.loans l
    WHERE l.customer_id=c.customer_id
);


-- ==========================================
-- TASK 7 : Correlated Subqueries
-- ==========================================

-- 1. Employees earning above branch average

SELECT *
FROM banking.employees e

WHERE salary >
(
    SELECT AVG(salary)
    FROM banking.employees
    WHERE branch_id=e.branch_id
);

-- 2. Loans above average of same loan type

SELECT *
FROM banking.loans l

WHERE loan_amount >
(
    SELECT AVG(loan_amount)
    FROM banking.loans
    WHERE loan_type=l.loan_type
);

-- 3. Payments above average payment of same loan

SELECT *
FROM banking.loan_payments p

WHERE payment_amount >
(
    SELECT AVG(payment_amount)
    FROM banking.loan_payments
    WHERE loan_id=p.loan_id
);

-- 4. Every customer with number of loans

SELECT
c.customer_id,
c.full_name,

(
SELECT COUNT(*)
FROM banking.loans l
WHERE l.customer_id=c.customer_id
)

AS total_loans

FROM banking.customers c;


-- 5. Every branch with number of employees

SELECT
b.branch_id,
b.branch_name,

(
SELECT COUNT(*)
FROM banking.employees e
WHERE e.branch_id=b.branch_id
)

AS total_employees

FROM banking.branches b;


-- ==========================================
-- TASK 8 : Explanation Comments
-- ==========================================

-- Scalar Subquery:
-- Returns only one value (one row and one column).

-- Correlated Subquery:
-- Uses a value from the outer query and executes once for every outer row.

-- EXISTS:
-- Useful when checking whether at least one related row exists.

-- NOT EXISTS:
-- Safer than NOT IN because it handles NULL values correctly.