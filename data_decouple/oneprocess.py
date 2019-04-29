import os
import datetime
import dateutil.parser
import requests as request_lib
import websocket
import json
from collections import deque

websocket_url = "wss://ws-feed.pro.coinbase.com"
subscribe_message = {
    "type": "subscribe",
    "product_ids": [
        "BTC-USD"
    ]
}

def get_data(collect_amount):
    new_trades = deque(maxlen = collect_amount)
    data_socket = websocket.create_connection(websocket_url)
    data_socket.send(json.dumps(subscribe_message))
    live_prices = 0
    responses = 0
    while live_prices <= collect_amount:
        new_feed_info = data_socket.recv()
        new_data = json.loads(new_feed_info)
        if new_data["type"] == "match":
            live_prices += 1
            print(new_data["price"])
            new_trades.append(new_data["price"])
        responses += 1
    return new_trades


TRADES_TO_GATHER = 5
start_time = datetime.datetime.now()
trade_holder = get_data(TRADES_TO_GATHER)
#signal_to_noise = get_data()
end_time = datetime.datetime.now()
run_time = end_time - start_time
print("It took", run_time, "to collect", TRADES_TO_GATHER, "trades")
#print("the SNR is", signal_to_noise, "%")
