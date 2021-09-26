# Write your MySQL query statement below

# 320ms

SELECT FirstName, LastName, City, State
FROM Person
LEFT JOIN Address
ON Person.PersonID=Address.PersonID;

