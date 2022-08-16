# Write your MySQL query statement below
SELECT w2.id id
FROM Weather w1, Weather w2
WHERE DATEDIFF(w2.recordDate, w1.recordDate)= 1 and w2.temperature > w1.temperature
