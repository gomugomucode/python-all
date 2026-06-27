-- ==========================================
-- DAY 7 : SET OPERATIONS & FINAL BUSINESS REPORT
-- ==========================================

-- ==========================================
-- TASK 1 : UNION
-- Unique cities from Customers, Branches and Employees
-- ==========================================

SELECT city
FROM banking.customers

UNION

SELECT city
FROM banking.branches

UNION

SELECT DISTINCT b.city
FROM banking.employees e
JOIN banking.branches b
ON e.branch_id = b.branch_id;


-- ==========================================
-- TASK 2 : UNION ALL
-- Customer and Employee Names
-- ==========================================

SELECT
full_name AS name,
'CUSTOMER' AS record_type
FROM banking.customers

UNION ALL

SELECT
full_name,
'EMPLOYEE'
FROM banking.employees;


-- ==========================================
-- TASK 3 : INTERSECT
-- Cities appearing in both tables
-- ==========================================

SELECT city
FROM banking.customers

INTERSECT

SELECT city
FROM banking.branches;


-- ==========================================
-- TASK 4 : EXCEPT
-- ==========================================

-- Customer cities without branches

SELECT city
FROM banking.customers

EXCEPT

SELECT city
FROM banking.branches;


-- Branch cities without customers

SELECT city
FROM banking.branches

EXCEPT

SELECT city
FROM banking.customers;



-- ==========================================
-- TASK 5 : Customer Loan Summary
-- ==========================================

SELECT

c.customer_id,
c.full_name,

COUNT(DISTINCT l.loan_id) AS total_loans,

COALESCE(SUM(DISTINCT l.loan_amount),0) AS total_loan_amount,

COALESCE
(
(
SELECT SUM(payment_amount)
FROM banking.loan_payments p
WHERE p.loan_id IN
(
SELECT loan_id
FROM banking.loans
WHERE customer_id=c.customer_id
)
AND payment_status='COMPLETED'
),0
)

AS total_completed_payment

FROM banking.customers c

LEFT JOIN banking.loans l
ON c.customer_id=l.customer_id

GROUP BY
c.customer_id,
c.full_name

ORDER BY c.customer_id;



-- =======================