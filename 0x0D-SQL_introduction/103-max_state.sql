-- Displays the max temp of each state.
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY max_temp ORDER BY state DESC;
