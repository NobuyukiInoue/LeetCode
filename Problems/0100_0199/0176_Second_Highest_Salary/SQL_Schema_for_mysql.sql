create database If Not Exists LeetCode;
show databases;

use LeetCode;

Create table If Not Exists Employee (Id int, Salary int);
show tables;

Truncate table Employee;
insert into Employee (Id, Salary) values ('1', '100');
insert into Employee (Id, Salary) values ('2', '200');
insert into Employee (Id, Salary) values ('3', '300');
select * from Employee;
