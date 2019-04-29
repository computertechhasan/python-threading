import os
import datetime
import dateutil.parser
import requests as request_lib
import websocket
import json
from collections import deque
import threading


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
    print("data pid is", os.getpid())
    while live_prices <= collect_amount:
        new_feed_info = data_socket.recv()
        new_data = json.loads(new_feed_info)
        if new_data["type"] == "match":
            live_prices += 1
            pipe.send(new_data["price"])
        responses += 1
    #return new_trades
def find_moving_average():
    new_trades = deque(maxlen = collect_amount)
    curr_data_received = 0
    print("math pid is", os.getpid())
    start_time = datetime.datetime.now()
    while curr_data_received < collect_amount:
        new_data = pipe.recv()
        print(new_data)
        if new_data:
            new_trades.append(new_data)
            curr_data_received += 1
    end_time = datetime.datetime.now()
    run_time = end_time - start_time
    print("It took", run_time, "to collect", TRADES_TO_GATHER, "trades")
    #for trade in new_trades:
        #print(trade)



TRADES_TO_GATHER = 5

#trade_holder = get_data(TRADES_TO_GATHER)
trade_holder = deque(maxlen = TRADES_TO_GATHER)
data_thread = threading.Thread(target = get_data, args = (TRADES_TO_GATHER))
math_thread = threading.Thread(target = take_data_from_pipe, args = (TRADES_TO_GATHER))

data_thread.start()
math_thread.start()
#signal_to_noise = get_data()

#print("the SNR is", signal_to_noise, "%")