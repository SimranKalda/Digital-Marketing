# Digital Marketing Analytics Dashboard

This **Digital Marketing Analytics Dashboard** helps to track the performance of your digital marketing campaigns. It brings together all the important metrics—like impressions, clicks, conversions, and cost-per-click—into one place, so you can easily see how your campaigns are doing and make data-driven decisions.

**Metrics 
- **Track Impressions & Clicks**: See how many impressions and clicks you got, with trends over time to spot patterns.
- **Click-Through Rate (CTR)**: Check the click-through rate (CTR) for your campaigns and see how well your ads are engaging users.
- **Cost Per Click (CPC)**: Understand how much you’re paying per click and get insights into your ad spend.
- **Conversions**: See how many conversions (purchases, sign-ups, etc.) your campaigns are driving.
- **Campaign Performance**: Break down conversions by different campaigns to see which ones are performing the best.
- **Marketing Funnel**: Visualize how users move through your marketing funnel, from seeing your ad to converting.
- **Day of the Week Performance**: Check which days are driving the most conversions, so you can optimize your campaigns.
- **Device Breakdown**: See how performance varies across different devices (mobile, tablet, computer).
- **Network Breakdown**: See which ad networks (like Google Search or Display Network) are getting you the most impressions.


This dashboard uses data about your digital marketing activities, including:

- **Impressions**: How many times your ad was shown.
- **Clicks**: How many times people clicked on your ad.
- **Conversions**: How many successful actions (like sign-ups or purchases) resulted from your campaign.
- **Campaign Details**: Information about your different campaigns (e.g., 'UK|Generic|Cake').
- **Device Type**: Whether users clicked on your ad using a mobile phone, tablet, or computer.
- **Ad Network**: Where your ads were shown (e.g., Google Search, Display Network).

Tech:
- **Power BI**: Power BI to create the dashboard and make everything interactive so you can dig into the details.
- **SQL**: For querying the data and transforming it into a usable format.
- **Python**: Used for cleaning and preparing the data before it’s put into the dashboard.


- **Quick Metrics**: You’ll see your key stats—Impressions, Clicks, Conversions, CTR, CPC—right at the top. These numbers give you an overview of how your campaigns are performing.
- **Trends Over Time**: Hover over the graph to see daily changes in impressions and clicks.
- **Campaign Breakdown**: The “Conversion by Campaign” chart will show you how different campaigns are performing.
- **Weekday Performance**: Want to know which days are driving the most conversions? The weekday chart tells you which days perform the best.
- **Device Comparison**: See how each device type (Mobile, Tablet, Computer) is performing in terms of impressions, clicks, and conversions.
- **Network Insights**: View how different ad networks (Google, Display Network, etc.) compare in terms of impressions.
  
## Cleaning the Data

Before the data can be used in the dashboard, it needs to go through a cleaning process. Here’s how we do it:

1. **Remove duplicates**: We make sure there are no repeated rows.
2. **Handle missing data**:
   - We drop rows with missing important columns (like `date` or `campaign`).
   - We fill missing numerical columns like `cost` with the median or the most common value.
   - Categorical columns with missing values are filled with 'Unknown'.
3. **Correct data types**: We check if columns have the right types (e.g., `cost` should be a number, `date` should be a date).
4. **Remove outliers**: We get rid of any weird data points, like negative clicks or impressions.
5. **Reformat data**: We make sure the `date` column is in the right format for analysis.
6. **Reset index**: After cleaning, we reset the dataset's index for a fresh start.

