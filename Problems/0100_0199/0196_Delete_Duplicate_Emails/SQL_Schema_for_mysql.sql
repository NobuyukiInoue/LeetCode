Create database If Not Exists LeetCode;
show databases;
use LeetCode;

Create table If Not Exists Person (Id int, Email varchar(255));
show tables;

Truncate table Person;

insert into Person (Id, Email) values ('1', 'john@example.com');
insert into Person (Id, Email) values ('2', 'bob@example.com');
insert into Person (Id, Email) values ('3', 'john@example.com');

select * from Person;
