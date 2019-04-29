import os
import datetime
import dateutil.parser
import requests as request_lib
import websocket
import json

websocket_url = "wss://ws-feed.pro.coinbase.com"
subscribe_message = {
    "type": "subscribe",
    "product_ids": [
        "BTC-USD"
    ]
}

def get_data():
    data_socket = websocket.create_connection(websocket_url)
    data_socket.send(json.dumps(subscribe_message))
    live_prices = 0
    responses = 0
    while live_prices < 5:
        new_feed_info = data_socket.recv()
        #start_time = datetime.datetime.now()
        new_data = json.loads(new_feed_info)
        if new_data["type"] == "match":
            live_prices += 1
        #end_time = datetime.datetime.now()
        responses += 1
    return (live_prices / responses) * 100

#run_time = get_data()
signal_to_noise = get_data()
#print("The parsing took", run_time.microseconds, "microseconds")
print("the SNR is", signal_to_noise, "%")








