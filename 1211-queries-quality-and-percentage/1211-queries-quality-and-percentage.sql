# Write your MySQL query statement below
SELECT query_name, ROUND(SUM(rating/position) / COUNT(*), 2) quality, ROUND(SUM(rating < 3) * 100/COUNT(*), 2) poor_query_percentage
FROM Queries
GROUP BY 1
