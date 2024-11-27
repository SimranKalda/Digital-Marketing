SELECT campaign, 
       SUM(cost) / COUNT(DISTINCT conversion_id) AS cost_per_conversion
FROM marketing_data
WHERE conversion_id IS NOT NULL
GROUP BY campaign
ORDER BY cost_per_conversion DESC;
