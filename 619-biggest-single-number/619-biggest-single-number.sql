# Write your MySQL query statement below
SELECT (SELECT num
        FROM MyNumbers
        Group By num
        HAVING count(*) = 1
        
        UNION ALL
        SELECT NULL
        
        ORDER BY num DESC Limit 1) num