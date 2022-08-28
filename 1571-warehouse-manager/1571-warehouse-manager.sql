# Write your MySQL query statement below
SELECT name warehouse_name, SUM(units * Width * Length * Height) volume
FROM Warehouse w
JOIN Products p ON w.product_id = p.product_id
GROUP BY 1
