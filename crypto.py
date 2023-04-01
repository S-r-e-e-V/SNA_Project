import cbpro
import pandas as pd
import datetime
import matplotlib.pyplot as plt

public_client = cbpro.PublicClient()


# start_date = pd.Timestamp('2022-03-25')
# end_date = pd.Timestamp('2023-03-25')
start_date = datetime.datetime(2022, 1, 1)
end_date = datetime.datetime(2022, 5, 1)
delta = pd.Timedelta('1 day')
dates = pd.date_range(start_date, end_date, freq=delta).to_pydatetime().tolist()

# print(public_client.get_product_historic_rates("BTC-USD"));

df = pd.DataFrame(public_client.get_product_historic_rates(
    'ETH-USDT',start=start_date,end=end_date,granularity=86400
))

# df = pd.DataFrame(public_client.get_product_historic_rates(
#     'BTC-USD', 
#     start_date, 
#     end_date,
#     granularity=86400  # 1 day
# ))


df.columns = ['time', 'low', 'high', 'open', 'close', 'volume']

df['time'] = pd.to_datetime(df['time'], unit='s')
df = df.set_index('time')

df1 = pd.DataFrame(public_client.get_product_historic_rates(
    'BTC-USDT',start=start_date,end=end_date,granularity=86400
))

# df1 = pd.DataFrame(public_client.get_product_historic_rates(
#     'BTC-USD', 
#     start_date, 
#     end_date,
#     granularity=86400  # 1 day
# ))


df1.columns = ['time', 'low', 'high', 'open', 'close', 'volume']

df1['time'] = pd.to_datetime(df1['time'], unit='s')
df1 = df1.set_index('time')


# Set the start and end dates for the time range to highlight
start_date = '2022-01-10'
end_date = '2022-03-15'

start_date1 = '2022-03-20'
end_date1 = '2022-04-15'

# Create a figure and an axis object
fig, ax = plt.subplots(figsize=(12,6))

# Plot the data on the axis object
ax.plot(df['close'])
ax.set_title('ETH-USDT')
ax.set_xlabel('Date')
ax.set_ylabel('Price (USD)')

# Use axvspan() to highlight the time range
ax.axvspan(start_date, end_date, color='green', alpha=0.2,label="Happy")
ax.axvspan(start_date1, end_date1, color='blue', alpha=0.2,label="Sad")

ax.legend()

# Show the plot
plt.show()