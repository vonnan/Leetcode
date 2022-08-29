# Write your MySQL query statement below
SELECT
    s.seller_name seller_name
FROM seller s
LEFT JOIN orders o
ON o.seller_id = s.seller_id AND YEAR(o.sale_date) = "2020"
WHERE o.seller_id IS NULL
ORDER BY 1