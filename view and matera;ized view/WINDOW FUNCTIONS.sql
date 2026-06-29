
-- DAY 4 – WINDOW FUNCTIONS
-- Q16. ROW_NUMBER(), RANK(), and DENSE_RANK()

SELECT
    account_id,
    acct_crncy_code,
    account_balance,

    ROW_NUMBER() OVER (
        PARTITION BY acct_crncy_code
        ORDER BY account_balance DESC
    ) AS row_num,

    RANK() OVER (
        PARTITION BY acct_crncy_code
        ORDER BY account_balance DESC
    ) AS rnk,

    DENSE_RANK() OVER (
        PARTITION BY acct_crncy_code
        ORDER BY account_balance DESC
    ) AS dense_rnk

FROM account
WHERE acct_cls_flg = 'N'
ORDER BY acct_crncy_code, account_balance DESC;

-- Q17. Average Balance and Difference

SELECT
    a.account_id,
    c.cust_name,
    a.acct_crncy_code,
    a.account_balance,

    ROUND(
        AVG(a.account_balance)
        OVER (PARTITION BY a.acct_crncy_code),
        2
    ) AS avg_balance,

    ROUND(
        a.account_balance -
        AVG(a.account_balance)
        OVER (PARTITION BY a.acct_crncy_code),
        2
    ) AS diff

FROM account a
JOIN customer c
    ON a.cust_id = c.cust_id
WHERE a.acct_cls_flg = 'N'
ORDER BY a.acct_crncy_code, a.account_balance DESC;

-- Q18. Top 3 Accounts per Province using RANK()

WITH ranked_accounts AS (
    SELECT
        b.province,
        b.branch_name,
        c.cust_name,
        a.account_id,
        a.account_balance,

        RANK() OVER (
            PARTITION BY b.province
            ORDER BY a.account_balance DESC
        ) AS rnk

    FROM account a
    JOIN customer c
        ON a.cust_id = c.cust_id
    JOIN branch b
        ON a.branch_id = b.branch_id
    WHERE a.acct_cls_flg = 'N'
)

SELECT
    province,
    branch_name,
    cust_name,
    account_id,
    account_balance,
    rnk
FROM ranked_accounts
WHERE rnk <= 3
ORDER BY province, rnk;

-- Q19. DENSE_RANK() by Account Type

SELECT
    account_id,
    schm_type,
    account_balance,

    DENSE_RANK() OVER (
        PARTITION BY schm_type
        ORDER BY account_balance DESC
    ) AS dense_rnk

FROM account
WHERE acct_cls_flg = 'N'
ORDER BY schm_type, dense_rnk;
Answer

-- The DENSE_RANK of the second-highest FD account depends on your database data.

-- Run the above query and look for the second-highest balance in the FD (schm_type = 'FD') group.

-- Q20. Final Challenge (Combining All Days)
    
WITH base AS (
    SELECT
        a.account_id,
        a.account_balance,
        a.acct_crncy_code,
        c.cust_name,
        b.branch_name,
        b.province
    FROM account a
    JOIN customer c
        ON a.cust_id = c.cust_id
    JOIN branch b
        ON a.branch_id = b.branch_id
    WHERE a.acct_cls_flg = 'N'
      AND a.acct_crncy_code = 'NPR'
),

ranked AS (
    SELECT
        *,
        RANK() OVER (
            PARTITION BY province
            ORDER BY account_balance DESC
        ) AS rnk,

        AVG(account_balance)
        OVER (
            PARTITION BY province
        ) AS province_avg

    FROM base
)

SELECT
    province,
    branch_name,
    cust_name,
    account_balance,
    rnk,
    ROUND(province_avg, 2) AS province_avg
FROM ranked
WHERE rnk = 1
ORDER BY province;
