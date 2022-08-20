# Write your MySQL query statement below
SELECT u.name, SUM(t.amount) balance
FROM Transactions t
JOIN Users u ON t.account = u.account
GROUP BY 1
HAVING balance >= 10000
