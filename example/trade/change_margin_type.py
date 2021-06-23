'''
Author: your name
Date: 2021-06-23 07:52:32
LastEditTime: 2021-06-23 08:03:49
LastEditors: your name
Description: In User Settings Edit
FilePath: /binance_sdk/example/trade/change_margin_type.py
'''
from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *
from binance_f.model.constant import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
result = request_client.change_margin_type(symbol="BTCUSDT", marginType=FuturesMarginType.ISOLATED)

PrintBasic.print_obj(result)
