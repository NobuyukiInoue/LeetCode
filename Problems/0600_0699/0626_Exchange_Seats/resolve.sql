# Write your MySQL query statement below

# 263ms - 466ms

SELECT
IF(id < (select count(*) from Seat), IF(id mod 2=0, id-1, id+1), IF(id mod 2=0, id-1, id)) AS id, student
FROM Seat
ORDER BY id ASC;
