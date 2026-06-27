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

