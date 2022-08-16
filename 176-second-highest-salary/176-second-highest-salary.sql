# Write your MySQL query statement below
select (SELECT DISTINCT salary 
FROM Employee e
ORDER by 1 DESC
LIMIT 1, 1) SecondHighestSalary
