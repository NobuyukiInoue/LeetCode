create database If Not Exists LeetCode;
show databases;

use LeetCode;

Create table If Not Exists Tree (id int, p_id int);

show tables;

Truncate table Tree;

insert into Tree (id, p_id) values ('1', 'None');
insert into Tree (id, p_id) values ('2', '1');
insert into Tree (id, p_id) values ('3', '1');
insert into Tree (id, p_id) values ('4', '2');
insert into Tree (id, p_id) values ('5', '2');

select * from Tree;
