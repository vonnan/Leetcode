# Write your MySQL query statement below
SELECT employee_id 
FROM 
    (select * from Employees left join Salaries USING (employee_id)
    union
    select * from Employees right join Salaries USING (employee_id)) n
WHERE name is NULL or salary is NULL
ORDER BY employee_id