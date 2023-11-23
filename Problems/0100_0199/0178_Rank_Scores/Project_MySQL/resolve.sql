# Write your MySQL query statement below

# 431ms - 445ms

SELECT score, dense_rank() OVER(ORDER BY score DESC) AS "rank"
  FROM Scores;
