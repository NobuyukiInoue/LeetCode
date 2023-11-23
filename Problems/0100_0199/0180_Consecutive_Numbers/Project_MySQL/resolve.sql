# Write your MySQL query statement below

# 817ms - 1046ms

WITH cte AS (
    SELECT num,
    lead(num,1) over() num1,
    lead(num,2) over() num2
    FROM Logs
)
SELECT DISTINCT num ConsecutiveNums FROM cte WHERE (num = num1) AND (num = num2);
