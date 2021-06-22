import hmac
import hashlib
from urllib import parse
import time
from datetime import datetime, timedelta
import requests
import pandas as pd
import numpy as np
import os

key = "2dikJ7QGkZOOcsymXw3r1rHpRHsMgl7UsDsVCg3AS7WU9QgtuoUA2kX2XtWLE6Pj"
secret = "LHBYf2ZKI6cmpbOtxfxpd79UIGlDpE6wvrWWMBAgrxImtS9D4NGht72ieRKXvFim"
id_path = "https://api.binance.com/sapi/v1/futuresHistDataId"
link_path = "https://api.binance.com/sapi/v1/downloadLink"

query_symbols = ['BTCUSDT','ETHUSDT','LTCUSDT','EOSUSDT']

def sign(params:dict,secret:str):
    query = parse.urlencode(sorted(params.items()))
    secret = secret.encode()
    signature = hmac.new(secret, query.encode("utf-8"), hashlib.sha256).hexdigest()
    return signature

headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
            "X-MBX-APIKEY": key
        }

def get_query_path(path, params):
    timestamp = int(time.time()*1000)
    params["timestamp"] = timestamp+60000
    query = parse.urlencode(sorted(params.items()))
    signature = sign(params, secret)
    query += "&signature={}".format(signature)
    query_path = path + '?' + query
    return query_path

def request_post(path, headers):
    response = requests.request('POST', path, headers=headers)
    return response
def request_get(path, headers):
    response = requests.request('GET', path, headers=headers)
    return response

def geterate_periods(start='2020-01-01 00:00:00', end='2021-04-05 00:00:00', days=15):

    if end:
        endArray = time.strptime(end, "%Y-%m-%d %H:%M:%S")
        end = int(time.mktime(endArray)) * 1000
    else:
        end = int(time.time()) * 1000

    startArray = time.strptime(start, "%Y-%m-%d %H:%M:%S")
    start = int(time.mktime(startArray)) * 1000
    return range(start, end, days*24*60*60*1000)

def get_symbol_start(csv_file,symbol,data_type,days):
    if not os.path.exists(csv_file):
        time_start = int(time.mktime(datetime.strptime('2020-01-01','%Y-%m-%d').timetuple())) * 1000
    else:
        df = pd.read_csv(csv_file)
        time_s= df[(df['symbol'] == symbol)&(df['dataType']==data_type)]['start'].max()
        if time_s is np.nan:
            time_start = int(time.mktime(datetime.strptime('2020-01-01','%Y-%m-%d').timetuple())) * 1000
        else:
            time_p = datetime.strptime(time_s,'%Y-%m-%d') + timedelta(days=days)
            time_start = int(time.mktime(time_p.timetuple())) * 1000
    return time_start


def run_id(csv_file, days):
    for symbol in query_symbols:
        if symbol == 'BTCUSDT':
            data_type_list = ['T_TRADE','S_DEPTH']
        else:
            data_type_list = ['T_TRADE']
        for data_type in data_type_list:
            time_start = get_symbol_start(csv_file, symbol, data_type,days)
            while time_start < int(time.mktime(datetime.today().timetuple()))*1000:
                start = time_start
                end = start + days * 24 * 60 * 60 * 1000
                params = {
                'symbol': symbol,
                'startTime': str(start),
                'endTime': str(end),
                'dataType': data_type,
                'recvWindow':60000
                }
                query_path_ = get_query_path(id_path, params)
                ret = request_post(query_path_, headers)
                print(ret.text)
                if ret.status_code == 200:
                    ret_id = ret.json()['id']
                    result_dic = {
                        'symbol':symbol,
                        'start':datetime.fromtimestamp(start/1000),
                        'dataType':data_type,
                        'id':ret_id
                    }
                    df = pd.DataFrame(result_dic, index=[0])
                    if not os.path.exists(csv_file):
                        df.to_csv(csv_file, index=False, mode='a')
                    else:
                        df.to_csv(csv_file, index=False, mode='a', header=False)
                    time_start = end
                else:
                    time.sleep(1800)

if __name__ == '__main__':
    csv_file = './result_id.csv'
    days = 7
    run_id(csv_file, days)