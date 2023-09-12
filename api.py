import requests
import json

cotacoes = requests.get( https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL)
cotacoes = requests.json()
cotacoes_dolar = cotacoes['USD']["bid"]
cotacoes_bit = cotacoes['BTCBRL']["bid"]
print(cotacoes_dolar)
print(cotacoes_bit)