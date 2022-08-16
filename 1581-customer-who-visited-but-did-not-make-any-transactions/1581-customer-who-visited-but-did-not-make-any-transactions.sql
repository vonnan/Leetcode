# Write your MySQL query statement below
select customer_id, count(*) count_no_trans
FROM Visits v
LEFT JOIN Transactions t ON t.visit_id = v.visit_id
WHERE t.amount is NULL
GROUP BY customer_id