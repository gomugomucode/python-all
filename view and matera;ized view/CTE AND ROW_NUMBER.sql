-- DAY 3 – CTE AND ROW_NUMBER()
-- Q11. CTE: Count Active Accounts by Currency

WITH active_accounts AS (
    SELECT *
    FROM account
    WHERE acct_cls_flg = 'N'
)

SELECT
    acct_crncy_code,
    COUNT(*) AS total_active_accounts
FROM active_accounts
GROUP BY acct_crncy_code
ORDER BY total_active_accounts DESC;

-- Q12. ROW_NUMBER(): Rank Active Accounts for Each Customer

SELECT
    cust_id AS customer_id,
    account_id,
    account_balance,
    acct_crncy_code,
    ROW_NUMBER() OVER (
        PARTITION BY cust_id
        ORDER BY account_balance DESC
    ) AS rn
FROM account
WHERE acct_cls_flg = 'N';

-- Q13. Highest Balance Active Account for Each Branch

WITH ranked_accounts AS (
    SELECT
        a.branch_id,
        a.account_id,
        c.cust_name,
        a.account_balance,
        ROW_NUMBER() OVER (
            PARTITION BY a.branch_id
            ORDER BY a.account_balance DESC
        ) AS rn
    FROM account a
    JOIN customer c
        ON a.cust_id = c.cust_id
    WHERE a.acct_cls_flg = 'N'
)

SELECT
    branch_id,
    account_id,
    cust_name,
    account_balance
FROM ranked_accounts
WHERE rn = 1;

-- Q14. High Balance CTE

WITH high_balance AS (
    SELECT *
    FROM account
    WHERE acct_cls_flg = 'N'
      AND account_balance > 300000
)

SELECT
    c.cust_name,
    h.account_id,
    h.account_balance,
    c.nationality
FROM high_balance h
JOIN customer c
    ON h.cust_id = c.cust_id
ORDER BY h.account_balance DESC;

    -- --  Answer:
    -- The number of rows depends on the data in your database. After running the query, count the returned rows (or use COUNT(*) if your instructor specifically asks for the number).

-- Q15. Two Chained CTEs
WITH active_npr AS (
    SELECT *
    FROM account
    WHERE acct_cls_flg = 'N'
      AND acct_crncy_code = 'NPR'
),

ranked AS (
    SELECT
        *,
        ROW_NUMBER() OVER (
            PARTITION BY cust_id
            ORDER BY account_balance DESC
        ) AS rn
    FROM active_npr
)

SELECT
    cust_id AS customer_id,
    account_id,
    account_balance,
    rn
FROM ranked
WHERE rn <= 2
ORDER BY customer_id, rn;