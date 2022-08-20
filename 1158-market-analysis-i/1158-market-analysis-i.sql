# Write your MySQL query statement below
SELECT u.user_id buyer_id, u.join_date, COUNT(o.order_id) orders_in_2019
FROM Users u 
LEFT JOIN Orders o
ON o.buyer_id = u.user_id and YEAR(o.order_date) = "2019"
GROUP By 1
ORDER BY 1

