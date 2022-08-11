# Write your MySQL query statement below
SELECT player_id, device_id
FROM Activity
WHERE (player_id, event_date) in (select player_id, min(event_date)
                                  from Activity
                                  group by player_id)