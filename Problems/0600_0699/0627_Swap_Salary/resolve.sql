# Write your MySQL query statement below

# 268ms - 386ms

UPDATE Salary
    SET sex  = (CASE WHEN sex = 'm' 
        THEN  'f' 
        ELSE 'm' 
        END);

