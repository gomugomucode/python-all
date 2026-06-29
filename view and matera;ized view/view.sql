-- DAY 1 – VIEW
-- Q1. Create vw_active_accounts

CREATE VIEW vw_active_accounts AS
SELECT
    a.account_id,
    c.cust_name,
    b.branch_name,
    b.province,
    a.account_balance,
    a.acct_crncy_code
FROM account a
JOIN customer c
    ON a.cust_id = c.cust_id
JOIN branch b
    ON a.branch_id = b.branch_id
WHERE a.acct_cls_flg = 'N';

-- Q2. Query the View

SELECT *
FROM vw_active_accounts
WHERE account_balance > 200000
ORDER BY account_balance DESC;

-- Q3. Create vw_loan_customers

CREATE VIEW vw_loan_customers AS
SELECT
    c.cust_id,
    c.cust_name,
    c.nationality,
    SUM(a.account_balance) AS total_loan_balance
FROM customer c
JOIN account a
    ON c.cust_id = a.cust_id
WHERE a.schm_type = 'LD'
  AND a.acct_cls_flg = 'N'
GROUP BY
    c.cust_id,
    c.cust_name,
    c.nationality;

-- Q4. Create vw_branch_summary

CREATE VIEW vw_branch_summary AS
SELECT
    b.branch_id,
    b.branch_name,
    b.province,
    COUNT(a.account_id) AS total_active_accounts,
    ROUND(SUM(a.account_balance), 2) AS total_active_balance
FROM branch b
LEFT JOIN account a
    ON b.branch_id = a.branch_id
   AND a.acct_cls_flg = 'N'
GROUP BY
    b.branch_id,
    b.branch_name,
    b.province
ORDER BY total_active_balance DESC;

-- Q5. Drop the View

DROP VIEW vw_active_accounts;

-- Explanation

-- Dropping a view does not delete any actual data because a view only stores the SQL query, not the data itself.