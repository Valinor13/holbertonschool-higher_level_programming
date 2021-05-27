-- Displays the avg temp per city.
SELECT city, AVG(temperatures) AS avg_temp FROM hbtn_0c_0 GROUP BY city ORDER BY avg_temp DESC;
