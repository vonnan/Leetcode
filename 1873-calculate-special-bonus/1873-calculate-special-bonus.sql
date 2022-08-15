# Write your MySQL query statement below
SELECT employee_id, IF(employee_id%2 and name not LIKE "M%", salary, 0) bonus
FROM Employees
ORDER BY employee_id
