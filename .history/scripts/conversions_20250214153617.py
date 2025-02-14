import pandas as pd
import requests

def get_eth_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
    response = requests.get(url).json()
    return response['etherium']['usd']

def convert_eth_usd


def main():
    get_eth_price()