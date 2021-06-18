'''
Author: your name
Date: 2021-06-14 17:31:17
LastEditTime: 2021-06-15 22:11:28
LastEditors: your name
Description: In User Settings Edit
FilePath: /Binance_Futures_python/example/market/get_order_book.py
'''
from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *

request_client = RequestClient(api_key='6tXxrT4l3YZOMrV1Kx9LaPA5LWLxgcHAHZNNYPVZcIoaDYQm3jj7J2DHuncOpiOu', secret_key='f4BauhCc4aZ82Qzt8CGMyVd7jkcIZK7zEF3qLQdCbIBv7EQLIvsvhDpY7b80JjyL')

result = request_client.get_order_book(symbol = "BTCUSDT", limit = 10)
print("======= Order Book =======")
print("lastUpdateId: ", result.lastUpdateId)
print("=== Bids ===")
PrintMix.print_data(result.bids)
print("===================")
print("=== Asks ===")
PrintMix.print_data(result.asks)
print("===================")
print("====================================")
