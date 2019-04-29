import time
import asyncio
import requests as request_lib
import websocket


base_http_url = "https://api.pro.coinbase.com"
url_params = "/products/REP-USD/trades?limit=100"
request_url = base_http_url + url_params


async def get_data():
    loop = asyncio.get_event_loop()
    future = loop.run_in_executor(None, request_lib.get, request_url)
    print("Sending request now!")
    data_response = await future
    print(data_response.json())
    print("Received request now!")
    #fetch_trade_request = await request_lib.get(url = request_url)
    

def main():
    loop = asyncio.get_event_loop()
    print("Starting main")
    loop.run_until_complete(get_data())
    print("Main ended")



main()