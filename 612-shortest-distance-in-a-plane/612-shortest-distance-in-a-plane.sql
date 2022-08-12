# Write your MySQL query statement below
SELECT round(sqrt(min(pow(a.x- b.x, 2) + pow(a.y - b.y, 2))), 2) shortest
FROM Point2D a, Point2D b
WHERE (a.x, a.y) != (b.x, b.y)