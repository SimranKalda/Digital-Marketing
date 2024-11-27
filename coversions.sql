##Clicks and Conversions by Campaign

SELECT campaign, 
       COUNT(DISTINCT click_id) AS total_clicks, 
       COUNT(DISTINCT conversion_id) AS total_conversions
FROM marketing_data
GROUP BY campaign
ORDER BY total_conversions DESC;
