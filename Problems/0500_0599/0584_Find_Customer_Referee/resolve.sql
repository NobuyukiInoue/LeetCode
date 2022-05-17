# Write your MySQL query statement below

# 416ms - 580ms

SELECT Customer.name from Customer where Customer.id not in (select id from Customer where referee_id = 2);
