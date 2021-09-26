# Write your MySQL query statement below

# 173ms

select max(salary) SecondHighestSalary
from Employee 
where salary < (select max(salary) from Employee);

