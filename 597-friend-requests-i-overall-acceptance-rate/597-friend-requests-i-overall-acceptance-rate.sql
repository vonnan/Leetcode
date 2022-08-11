# Write your MySQL query statement below
SELECT 
IFNULL((select round(count(distinct requester_id, accepter_id)/count(distinct sender_id, send_to_id) , 2) 
       from FriendRequest, RequestAccepted ), 0) accept_rate