# Write your MySQL query statement below
SELECT contest_id, ROUND(COUNT(DISTINCT user_id)* 100/(SELECT Count(*) FROM Users), 2) percentage
FROM Register r

GROUP BY 1
ORDER BY 2 DESC, 1