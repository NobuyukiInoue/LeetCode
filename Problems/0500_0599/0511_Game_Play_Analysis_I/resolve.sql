# Write your MySQL query statement below
# 672ms - 782ms

select distinct player_id,min(event_date) as first_login from Activity group by player_id;
