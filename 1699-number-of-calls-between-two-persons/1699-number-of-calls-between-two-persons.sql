# Write your MySQL query statement below
SELECT LEAST(from_id, to_id) person1, GREATEST(from_id, to_id) person2, COUNT(duration) call_count, SUM(duration) total_duration
FROM Calls
GROUP BY 1,2
