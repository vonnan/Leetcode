# Write your MySQL query statement below
SELECT user_id, CONCAT(UPPER(SUBSTR(name,1,1)), LOWER(SUBSTR(name,2))) name
FROM Users
ORDER by user_id
