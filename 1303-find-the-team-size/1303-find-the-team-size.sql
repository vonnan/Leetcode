# Write your MySQL query statement below
select employee_id, n.size team_size
FROM Employee e
LEFT JOIN (SELECT team_id, count(*) size
FROM Employee 
GROUP BY 1) n
ON e.team_id = n.team_id

