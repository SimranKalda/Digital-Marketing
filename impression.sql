SELECT DATE(date) AS date,
       COUNT(DISTINCT impression_id) AS total_impressions,
       COUNT(DISTINCT conversion_id) AS total_conversions
FROM marketing_data
WHERE date BETWEEN '2024-09-01' AND '2024-10-01'
GROUP BY date
ORDER BY date;
