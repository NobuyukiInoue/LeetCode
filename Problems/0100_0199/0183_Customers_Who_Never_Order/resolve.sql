# Write your MySQL query statement below

# 1139ms - 1151ms

SELECT name AS Customers
  FROM Customers
  WHERE id
  NOT IN (SELECT customerId FROM Orders);
