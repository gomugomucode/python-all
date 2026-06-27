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



-- ==========================================
-- TASK 6 : Loan Balance Report
-- ==========================================

SELECT

l.loan_id,
c.full_name,
l.loan_type,
l.loan_amount,

COALESCE
(
SUM
(
CASE
WHEN p.payment_status='COMPLETED'
THEN p.payment_amount
ELSE 0
END
),
0
)

AS total_completed_payment,

l.loan_amount -

COALESCE
(
SUM
(
CASE
WHEN p.payment_status='COMPLETED'
THEN p.payment_amount
ELSE 0
END
),
0
)

AS remaining_amount

FROM banking.loans l

JOIN banking.customers c
ON l.customer_id=c.customer_id

LEFT JOIN banking.loan_payments p
ON l.loan_id=p.loan_id

GROUP BY

l.loan_id,
c.full_name,
l.loan_type,
l.loan_amount

ORDER BY l.loan_id;



-- ==========================================
-- TASK 7 : Payment Progress Classification
-- ==========================================

SELECT

l.loan_id,
c.full_name,
l.loan_amount,

COALESCE
(
SUM
(
CASE
WHEN p.payment_status='COMPLETED'
THEN p.payment_amount
ELSE 0
END
),
0
)

AS completed_payment,

l.loan_amount -

COALESCE
(
SUM
(
CASE
WHEN p.payment_status='COMPLETED'
THEN p.payment_amount
ELSE 0
END
),
0
)

AS remaining_amount,

CASE

WHEN
(
l.loan_amount -
COALESCE
(
SUM
(
CASE
WHEN p.payment_status='COMPLETED'
THEN p.payment_amount
ELSE 0
END
),
0
)
)<=0

THEN 'PAID'

WHEN
(
l.loan_amount -
COALESCE
(
SUM
(
CASE
WHEN p.payment_status='COMPLETED'
THEN p.payment_amount
ELSE 0
END
),
0
)
)
<
(l.loan_amount*0.25)

THEN 'NEARLY PAID'

WHEN
(
l.loan_amount -
COALESCE
(
SUM
(
CASE
WHEN p.payment_status='COMPLETED'
THEN p.payment_amount
ELSE 0
END
),
0
)
)
<
(l.loan_amount*0.75)

THEN 'IN PROGRESS'

ELSE 'MOSTLY UNPAID'

END

AS payment_progress

FROM banking.loans l

JOIN banking.customers c
ON l.customer_id=c.customer_id

LEFT JOIN banking.loan_payments p
ON l.loan_id=p.loan_id

GROUP BY
l.loan_id,
c.full_name,
l.loan_amount;



-- ==========================================
-- TASK 8 : Final Branch Performance Report
-- ==========================================

SELECT

b.branch_name,

COALESCE(e.employee_count,0) AS employee_count,

COALESCE(a.account_count,0) AS account_count,

COALESCE(l.loan_count,0) AS loan_count,

COALESCE(a.total_balance,0) AS total_account_balance,

COALESCE(l.total_loan_amount,0) AS total_loan_amount,

COALESCE(p.total_payment,0) AS total_completed_payment,

COALESCE(l.average_loan_amount,0) AS average_loan_amount

FROM banking.branches b

LEFT JOIN
(
SELECT
branch_id,
COUNT(*) employee_count
FROM banking.employees
GROUP BY branch_id
)e
ON b.branch_id=e.branch_id

LEFT JOIN
(
SELECT
branch_id,
COUNT(*) account_count,
SUM(balance) total_balance
FROM banking.accounts
GROUP BY branch_id
)a
ON b.branch_id=a.branch_id

LEFT JOIN
(
SELECT
branch_id,
COUNT(*) loan_count,
SUM(loan_amount) total_loan_amount,
ROUND(AVG(loan_amount),2) average_loan_amount
FROM banking.loans
GROUP BY branch_id
)l
ON b.branch_id=l.branch_id

LEFT JOIN
(
SELECT
l.branch_id,
SUM(p.payment_amount) total_payment
FROM banking.loan_payments p
JOIN banking.loans l
ON p.loan_id=l.loan_id
WHERE payment_status='COMPLETED'
GROUP BY l.branch_id
)p
ON b.branch_id=p.branch_id;

