-- DAY 2 – MATERIALIZED VIEW
-- Q6. Create mv_active_accounts
CREATE MATERIALIZED VIEW mv_active_accounts AS
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
WHERE a.acct_cls_flg = 'N'
WITH DATA;

-- Q7. Refresh the Materialized View

REFRESH MATERIALIZED VIEW mv_active_accounts;

-- Explanation
-- REFRESH MATERIALIZED VIEW updates the materialized view by re-running its query and storing the latest data, and should be run whenever the underlying tables have changed.

-- Q8. Create mv_branch_balance

CREATE MATERIALIZED VIEW mv_branch_balance AS
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
WITH DATA;
-- Q9. Query mv_branch_balance
SELECT *
FROM mv_branch_balance
WHERE province = 'Bagmati'
ORDER BY total_active_balance DESC;

-- Explanation

-- This query is faster because a materialized view stores the query results on disk, so PostgreSQL reads the precomputed data instead of recalculating joins and aggregations every time.

-- Q10. Difference Between VIEW and MATERIALIZED VIEW
-- Feature	VIEW	MATERIALIZED VIEW
-- Stores data?	No	Yes
-- Speed (complex queries)	Slower	Faster
-- Auto-updates?	Yes	No
-- Refresh needed?	No	Yes