create database If Not Exists LeetCode;
show databases;

use LeetCode;

Create table If Not Exists Customers (id int, name varchar(255));
Create table If Not Exists Orders (id int, customerId int);

show tables;

Truncate table Customers;
insert into Customers (id, name) values ('1', 'Joe');
insert into Customers (id, name) values ('2', 'Henry');
insert into Customers (id, name) values ('3', 'Sam');
insert into Customers (id, name) values ('4', 'Max');

select * from Customers;

Truncate table Orders;
insert into Orders (id, customerId) values ('1', '3');
insert into Orders (id, customerId) values ('2', '1');

select * from Orders;

/*
drop table Customers;
drop table Orders;
*/

