-- a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.

SELECT score, COUNT(*) AS number_of_records
FROM second_table
GROUP BY score
ORDER BY number_of_records DESC;
