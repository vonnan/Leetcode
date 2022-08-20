# Write your MySQL query statement below
SELECT s.product_id, p.product_name
FROM Sales s JOIN Product p ON p.product_id = s.product_id
GROUP BY 1
HAVING MIN(s.sale_date) >= "2019-01-01" and MAX(s.sale_date) <= "2019-03-31"