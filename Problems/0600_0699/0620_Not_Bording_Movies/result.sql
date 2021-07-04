# Write your MySQL query statement below

SELECT id, movie, description, rating
FROM cinema
WHERE description NOT LIKE 'boring' AND id%2 !=0
ORDER BY rating DESC;

