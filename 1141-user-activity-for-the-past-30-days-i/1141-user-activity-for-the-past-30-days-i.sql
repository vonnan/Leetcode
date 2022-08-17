# Write your MySQL query statement below
SELECT activity_date day, count(DISTINCT user_id) active_users
FROM Activity
WHERE 0 <= DATEDIFF('2019-07-27', activity_date) and  DATEDIFF('2019-07-27', activity_date) < 30
GROUP BY activity_date
