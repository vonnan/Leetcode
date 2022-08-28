# Write your MySQL query statement below
SELECT LEFT(trans_date, 7) month, 
        country, 
        COUNT(amount) trans_count, 
        SUM(state = "approved") approved_count, 
        SUM(amount) trans_total_amount, 
        SUM(Case 
            WHEN state = "approved" THEN amount
            ELSE 0
            END
            ) approved_total_amount
FROM Transactions
GROUP BY 1,2