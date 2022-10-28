# Write your MySQL query statement below

Select email as "Email" FROM Person p GROUP BY email HAVING COUNT(email) > 1