-- Lists the number of records with matching scores.
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;
