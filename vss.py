import requests
import csv
import pandas as pd
url='https://api.kucoin.com/api/v1/market/orderbook/level2_100?symbol=BTC-USDT'
response = requests.get(url)
response.encoding = 'utf-8'
json = response.json()
print(json.keys())
df = pd.DataFrame(json['data'])
# print(response.content)
# print(response.url)
# print(response.status_code)
# print(response.headers)
df.to_csv('file_name.csv')