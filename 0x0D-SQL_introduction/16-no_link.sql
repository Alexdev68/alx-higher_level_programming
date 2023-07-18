-- This script lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
SELECT IFNULL(score, 0) AS score, name FROM second_table ORDER BY score DESC
