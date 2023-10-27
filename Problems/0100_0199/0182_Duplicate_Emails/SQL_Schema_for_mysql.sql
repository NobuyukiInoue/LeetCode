create database If Not Exists LeetCode;
show databases;

use LeetCode;

Create table If Not Exists Person (id int, email varchar(255));

show tables;

Truncate table Person;
insert into Person (id, email) values ('1', 'a@b.com');
insert into Person (id, email) values ('2', 'c@d.com');
insert into Person (id, email) values ('3', 'a@b.com');

select * from Person;

/*
drop table Person;
*/

