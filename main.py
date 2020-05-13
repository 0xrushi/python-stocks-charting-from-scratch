#!python
"""
Author: r4#51c0debloOded
Email: rushic24@gmail.com
Repository: https://github.com/arkochhar/Technical-Indicators
Version: 1.0.0
License: GNU GENERAL PUBLIC LICENSE, Version 3, 29 June 2007

refrences:- 
https://www.learndatasci.com/tutorials/python-finance-part-3-moving-average-trading-strategy/
sentdex https://pythonprogramming.net/more-stock-data-manipulation-python-programming-for-finance/
https://pythonprogramming.net/advanced-matplotlib-graphing-charting-tutorial/
https://github.com/arkochhar/Technical-Indicators
"""

#import unittest
#import quandl
#import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
from mpl_finance import candlestick_ohlc
import matplotlib.ticker as mticker

from indicators import EMA, ATR, SuperTrend, MACD, HA, BBand, RSI, Ichimoku

df = pd.read_csv("/mnt/F/ArchHome/Documents/StockMarketPredicctors/data/zeel.csv", header=0 ,usecols=[2,4,5,6,8,10])
date_time = pd.to_datetime(df['date'])
plt.style.use('dark_background')

datemin = dt.datetime(2016, 1, 1)
datemax = dt.datetime(2019, 1, 2)

def print_transactions(t):
    s=0
    for i in range(len(t)-1):
        if t[i]==1.0 and t[i+1] ==-1.0:
            s+=closep[i]
            print("Sold at Rs.{0} on {1} totalamt= {2}".format(closep[i],mdates.num2date(date[i]),s))
        elif t[i]==-1.0 and t[i+1] ==1:
            s-=closep[i]
            print("Bought at Rs.{0} on {1} totalamt= {2}".format(closep[i],date[i],s))

if __name__ == "__main__":
    #x= EMA(df,'close',3,3)
    x=MACD(df,base='close')

    ax1 = plt.subplot2grid((6,1), (0,0), rowspan=1, colspan=1)
    ax2 = plt.subplot2grid((6,1), (1,0), rowspan=4, colspan=1)
    ax3 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1)

    ax2.set_ylabel('₹')
    ax2.xaxis_date()
    ax2.xaxis.set_major_formatter(plt.NullFormatter())
    ax2.xaxis.set_major_locator(mticker.MultipleLocator(14))

    #ax2.legend(loc='best')
    ax3.tick_params(labelrotation=45)
    ax3.xaxis.set_major_formatter(mdates.DateFormatter("%d-%m-%Y"))
    ax3.xaxis.set_major_locator(mticker.MultipleLocator(14))
    
    date = [mdates.datestr2num(d) for d in df['date']]
    highp = df['high']
    closep = df['close']
    lowp = df['low']
    openp = df['open']
    volumep= df['totaltradedquantity']
    
    ohlc=[]
    ohlc = zip(date,openp,highp,lowp,closep,volumep)
    
    trading_positions_raw = x['macd_12_26_9'] - x['signal_12_26_9']
    trading_positions = np.sign(trading_positions_raw)
    trading_positions_final = trading_positions.shift(1)

    
    candlestick_ohlc(ax2, ohlc,width=0.6,colorup='g', colordown='r')
    ax3.plot(date,trading_positions_final)
    ax1.plot(date,x['macd_12_26_9'])
    ax1.plot(date,x['signal_12_26_9'])

    print_transactions(trading_positions_final)
    plt.show()