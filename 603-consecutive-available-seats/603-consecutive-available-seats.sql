# Write your MySQL query statement below

SELECT DISTINCT a.seat_id
FROM Cinema a
JOIN Cinema b
ON abs(a.seat_id - b.seat_id) = 1 and a.free = 1 and b.free= 1
ORDER BY a.seat_id