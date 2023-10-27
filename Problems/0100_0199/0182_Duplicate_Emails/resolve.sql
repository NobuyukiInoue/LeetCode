# Write your MySQL query statement below

# 621ms - 852ms

SELECT email
  FROM Person
  GROUP BY email
  HAVING count(email) > 1;
