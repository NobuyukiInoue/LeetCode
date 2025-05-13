# Write your MySQL query statement below

# 312ms - 322ms

SELECT user_id,
       email
  FROM Users
  WHERE regexp_like(email, '^[a-zA-Z0-9_]+@[a-zA-Z]+.com$')
  ORDER BY user_id;
