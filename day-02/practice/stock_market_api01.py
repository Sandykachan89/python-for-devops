import requests

API_KEY = "UFDSYTYE9MVB4FCY" #step 1 get API key

api_url = "https://www.alphavantage.co/" # step 2 find base url


def get_stock_market_data(symbol,is_timeseries):
    query = f"query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url=api_url+query)
    for key, value in response.json().items():
        if is_timeseries:
            
            print(key,value)
        else:
            if key == "Time Series (Daily)":
                continue


symbol = input("Enter the Symbol you want for the Stock Market API eg. (AMZN, GOGL, IBM, etc)")
is_timeseries = True
get_stock_market_data(symbol,is_timeseries)