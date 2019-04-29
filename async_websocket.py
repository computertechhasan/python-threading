import time
import asyncio
import requests as request_lib
import websocket
import json


base_http_url = "https://api.pro.coinbase.com"
url_params = "/products/REP-USD/trades?limit=100"
request_url = base_http_url + url_params

websocket_url = "wss://ws-feed.pro.coinbase.com"
subscribe_message = {
    "type": "subscribe",
    "product_ids": [
        "REP-USD"
    ]
}


async def get_from_pipe(curr_socket):
    try:
        new_data = json.loads(curr_socket.recv())
        return new_data
    except Exception as e:
        print("Exceiption!", e)

async def get_data():
    loop = asyncio.get_event_loop()
    data_socket = websocket.create_connection(websocket_url)
    #future = loop.run_in_executor(None, data_socket.send, json.dumps(subscribe_message))
    print("Sending request now!")
    data_socket.send(json.dumps(subscribe_message))
    new_data = await loop.run_in_executor(None, data_socket.recv())
    print(json.loads(new_data))
    print("Received request now!")
    #data_response = await future
    #fetch_trade_request = await request_lib.get(url = request_url)
    

def main():
    loop = asyncio.get_event_loop()
    print("Starting main")
    loop.run_until_complete(get_data())
    print("Main ended")



main()