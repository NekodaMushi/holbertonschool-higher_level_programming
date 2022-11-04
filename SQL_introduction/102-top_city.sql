-- Displays the top 3 of cities temperature during July and August ordered by temperature
SELECT TOP city VALUES(avg_temp) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC
