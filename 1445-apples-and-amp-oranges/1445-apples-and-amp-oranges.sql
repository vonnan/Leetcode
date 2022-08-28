# Write your MySQL query statement below
SELECT s1.sale_date, s1.sold_num - s2.sold_num diff
FROM Sales s1, Sales s2 
WHERE s1.fruit = "apples" and s2.fruit = "oranges" and s1.sale_date = s2.sale_date