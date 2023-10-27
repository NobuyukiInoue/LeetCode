# Write your MySQL query statement below

# 961ms - 1247ms

SELECT teacher_id,count(DISTINCT subject_id) AS cnt
  FROM Teacher
  GROUP BY teacher_id;
