import cbpro
import pandas as pd
import datetime
import matplotlib.pyplot as plt

def getEmotionColor(string):
    if string=="Happy":
        return "green"
    elif string=="Sad":
        return "red"
    else:
        return "blue"

def getCryptoData():
    public_client = cbpro.PublicClient()
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
    return df, df1

def getEmotionsChart(df,df1,array):

    # Create a figure and an axis object
    fig, (ax1,ax2) = plt.subplots(1,2,figsize=(20,6), sharex=True)

    # Plot the data on the axis object
    ax1.plot(df['close'])
    ax1.set_title('ETH-USD')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Price (USD)')
    ax1.tick_params(axis='x', rotation=45)

    ax2.plot(df1['close'],label="BTC-USD")
    ax2.set_title('BTC-USDT')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Price (USD)')
    ax2.tick_params(axis='x', rotation=45)
    ax2.legend(loc="upper right")

    for i in array:
        ax1.axvspan(i["start_date"], i["end_date"], color=getEmotionColor(i["emotion"]), alpha=0.2)
        ax2.axvspan(i["start_date"], i["end_date"], color=getEmotionColor(i["emotion"]), alpha=0.2)

    ax1.legend(loc="upper right")
    ax1.legend()
    # Show the plot
    plt.show()


# main

array=[
    {
        "start_date":'2022-01-10',
        "end_date":'2022-02-15',
        "emotion":"Happy",

    },
    {
        "start_date":'2022-02-20',
        "end_date":'2022-03-15',
        "emotion":"Sad",
    },
    {
        "start_date":'2022-04-20',
        "end_date":'2022-05-01',
        "emotion":"Happy",
    },
    {
        "start_date":'2022-03-15',
        "end_date":'2022-03-20',
        "emotion":"Happy",
    },
]

df,df1=getCryptoData()
getEmotionsChart(df,df1,array)