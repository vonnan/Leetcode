# Write your MySQL query statement below

SELECT u.name name, IFNULL(SUM(r.distance),0) travelled_distance
FROM Users u
LEFT OUTER JOIN Rides r
ON u.id = r.user_id
GROUP BY 1, u.id
ORDER BY 2 DESC, 1
