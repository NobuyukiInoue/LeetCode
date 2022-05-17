# Write your MySQL query statement below

# 358ms - 823ms

SELECT id,
CASE
    WHEN p_id IS NULL THEN 'Root'
    WHEN id IN (SELECT DISTINCT p_id FROM Tree) THEN 'Inner'
    ELSE 'Leaf'
END AS  type
FROM Tree;
