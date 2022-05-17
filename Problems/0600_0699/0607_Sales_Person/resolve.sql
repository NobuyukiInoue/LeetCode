# Write your MySQL query statement below

# 980ms - 1028ms

SELECT DISTINCT name AS name FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT DISTINCT(Orders.sales_id) FROM Orders 
    INNER JOIN Company ON Orders.com_id = Company.com_id
    WHERE Company.name = 'RED'
);
