import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('/Users/simran28/Python Files/mkdata.csv')

df['date'] = pd.to_datetime(df['date'])

df_filtered = df[(df['date'] >= '2024-09-01') & (df['date'] <= '2024-10-01')]

#Clicks and Conversions by Campaign
campaign_performance = df_filtered.groupby('campaign').agg(
    total_clicks=('click_id', 'nunique'),
    total_conversions=('conversion_id', 'nunique')
).reset_index()

campaign_performance['conversion_rate'] = (campaign_performance['total_conversions'] / campaign_performance['total_clicks']) * 100

# 2. CTR (Click-Through Rate) by Device Type
ctr_by_device = df_filtered.groupby('device_type').agg(
    total_impressions=('impression_id', 'nunique'),
    total_clicks=('click_id', 'nunique')
).reset_index()

ctr_by_device['ctr'] = (ctr_by_device['total_clicks'] / ctr_by_device['total_impressions']) * 100

# 3. Conversion Funnel Analysis (Impression -> Click -> Interaction -> Conversion)
funnel = df_filtered.groupby('funnel_stage').agg(
    total_users=('user_id', 'nunique')
).reset_index()

# 4. Weekly Performance (Conversion counts per day of the week)
df_filtered['weekday'] = df_filtered['date'].dt.day_name()
weekly_performance = df_filtered.groupby('weekday').agg(
    total_conversions=('conversion_id', 'nunique')
).reset_index()

# Sort by conversion count to get the most performing days
weekly_performance['weekday'] = pd.Categorical(
    weekly_performance['weekday'],
    categories=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    ordered=True
)
weekly_performance = weekly_performance.sort_values('total_conversions', ascending=False)

# 5. Cost Per Conversion by Campaign
cost_per_conversion = df_filtered.groupby('campaign').agg(
    total_cost=('cost', 'sum'),
    total_conversions=('conversion_id', 'nunique')
).reset_index()

cost_per_conversion['cost_per_conversion'] = cost_per_conversion['total_cost'] / cost_per_conversion['total_conversions']

# Visualize the results

# 1. Clicks and Conversions by Campaign
plt.figure(figsize=(10, 6))
sns.barplot(x='total_clicks', y='campaign', data=campaign_performance, color='lightblue', label='Clicks')
sns.barplot(x='total_conversions', y='campaign', data=campaign_performance, color='lightgreen', label='Conversions')
plt.title('Clicks and Conversions by Campaign')
plt.xlabel('Count')
plt.ylabel('Campaign')
plt.legend()
plt.show()

# 2. CTR by Device Type
plt.figure(figsize=(8, 5))
sns.barplot(x='ctr', y='device_type', data=ctr_by_device, palette='Blues_d')
plt.title('Click-Through Rate (CTR) by Device Type')
plt.xlabel('CTR (%)')
plt.ylabel('Device Type')
plt.show()

# 3. Conversion Funnel Visualization
plt.figure(figsize=(8, 5))
sns.barplot(x='total_users', y='funnel_stage', data=funnel, palette='Blues')
plt.title('Conversion Funnel Analysis')
plt.xlabel('Number of Users')
plt.ylabel('Funnel Stage')
plt.show()

# 4. Weekly Performance
plt.figure(figsize=(10, 6))
sns.barplot(x='total_conversions', y='weekday', data=weekly_performance, palette='viridis')
plt.title('Weekly Conversion Performance')
plt.xlabel('Total Conversions')
plt.ylabel('Weekday')
plt.show()

# 5. Cost Per Conversion by Campaign
plt.figure(figsize=(10, 6))
sns.barplot(x='cost_per_conversion', y='campaign', data=cost_per_conversion, palette='Blues_r')
plt.title('Cost Per Conversion by Campaign')
plt.xlabel('Cost Per Conversion ($)')
plt.ylabel('Campaign')
plt.show()
