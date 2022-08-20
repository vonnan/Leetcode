# Write your MySQL query statement below
SELECT email Email
FROM Person
GROUP BY 1
HAVING COUNT(email) > 1