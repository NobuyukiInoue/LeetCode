create database If Not Exists LeetCode;
show databases;

use LeetCode;

Create table If Not Exists Logs (id int, num int);
show tables;

Truncate table Logs;
insert into Logs (id, num) values ('1', '1');
insert into Logs (id, num) values ('2', '1');
insert into Logs (id, num) values ('3', '1');
insert into Logs (id, num) values ('4', '2');
insert into Logs (id, num) values ('5', '1');
insert into Logs (id, num) values ('6', '2');
insert into Logs (id, num) values ('7', '2');
select * from Logs;

-- drop table Logs;
