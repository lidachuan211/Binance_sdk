'''
Author: your name
Date: 2021-06-14 17:31:17
LastEditTime: 2021-06-16 09:00:15
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /Binance_Futures_python/example/market/get_candlestick_data.py
'''
from binance_f import RequestClient
from binance_f.model import *
from binance_f.constant.test import *
from binance_f.base.printobject import *

request_client = RequestClient(api_key='2dikJ7QGkZOOcsymXw3r1rHpRHsMgl7UsDsVCg3AS7WU9QgtuoUA2kX2XtWLE6Pj', secret_key='LHBYf2ZKI6cmpbOtxfxpd79UIGlDpE6wvrWWMBAgrxImtS9D4NGht72ieRKXvFim')

result = request_client.get_recent_trades_list(symbol="BTCUSDT", limit=1000)
# result = request_client.get_old_trade_lookup(symbol="BTCUSDT" ,fromId =183299463,limit=100)
PrintMix.print_data(result)

# result = request_client.get_candlestick_data(symbol="BTCUSDT", interval=CandlestickInterval.MIN1, 
# 												startTime=None, endTime=None, limit=10)

print("======= Kline/Candlestick Data =======")
PrintMix.print_data(result)
print("======================================")
