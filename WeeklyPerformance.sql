SELECT DAYOFWEEK(date) AS weekday,
       COUNT(DISTINCT conversion_id) AS total_conversions
FROM marketing_data
WHERE date BETWEEN '2024-09-01' AND '2024-09-30'
GROUP BY weekday
ORDER BY total_conversions DESC;
