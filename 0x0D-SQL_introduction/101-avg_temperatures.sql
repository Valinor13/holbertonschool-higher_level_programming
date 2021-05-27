-- Displays the avg temp per city.
SELECT city, AVG(temperatures) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
