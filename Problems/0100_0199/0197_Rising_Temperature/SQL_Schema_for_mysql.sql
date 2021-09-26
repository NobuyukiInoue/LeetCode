Create database If Not Exists LeetCode;
show databases;
use LeetCode;

Create table If Not Exists Weather (Id int, RecordDate date, Temperature int);
show tables;

Truncate table Weather;

insert into Weather (Id, RecordDate, Temperature) values ('1', '2015-01-01', '10');
insert into Weather (Id, RecordDate, Temperature) values ('2', '2015-01-02', '25');
insert into Weather (Id, RecordDate, Temperature) values ('3', '2015-01-03', '20');
insert into Weather (Id, RecordDate, Temperature) values ('4', '2015-01-04', '30');

select * from Weather;
