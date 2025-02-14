import pandas as pd
import requests

def get_eth_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
    response = requests.get(url).json()
    return response['etherium']['usd']

def convert_eth_usd(input_csv, output_csv):
    df = pd.read_cvs(input_csv)

    eth_price = get_eth_price()

    if 'value' not in df.columns or 'gas_used' not in df.columns or 'gas_price' not in df.columns:
        raise ValueError("Missing required columns for operation. Excpecting following columns in csv: 'value', 'gas_used', or 'gas_price'")
    
    # Convert gas cost from GWEI to ETH
    df['gas_cost_eth'] = df['gas_used'] * (df['gas_price'] / 1e9)

    df['total_cost_usd'] = (df[])



def main():
    get_eth_price()