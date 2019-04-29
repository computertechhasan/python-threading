import os
import datetime
import dateutil.parser
import requests as request_lib
import websocket
import json
from collections import deque
from multiprocessing import Process, current_process, Pool, Pipe

websocket_url = "wss://ws-feed.pro.coinbase.com"
subscribe_message = {
    "type": "subscribe",
    "product_ids": [
        "BTC-USD"
    ]
}

SHORT_MA_LENGTH = 5
LONG_MA_LENGTH = 10

trade_holder = deque(maxlen = 10)

def get_data(collect_amount, pipe):
    new_trades = deque(maxlen = collect_amount)
    data_socket = websocket.create_connection(websocket_url)
    data_socket.send(json.dumps(subscribe_message))
    print("data pid is", os.getpid())
    while True:
        new_feed_info = data_socket.recv()
        new_data = json.loads(new_feed_info)
        if new_data["type"] == "match":
            pipe.send(new_data)

def find_moving_averages():
    short_ma_sum = 0
    long_ma_sum = 0
    short_moving_average = 0
    long_moving_average = 0
    for index, trade in enumerate(trade_holder):
        if index < SHORT_MA_LENGTH:
            short_ma_sum += float(trade["price"])
        if index < LONG_MA_LENGTH:
            long_ma_sum += float(trade["price"])
        if index == LONG_MA_LENGTH:
            break
    short_moving_average = short_ma_sum / SHORT_MA_LENGTH
    long_moving_average = long_ma_sum / LONG_MA_LENGTH

def take_data_calc_ma(collect_amount, pipe):
    curr_data_received = 0
    print("math pid is", os.getpid())
    short_ma_sum = 0
    long_ma_sum = 0
    short_moving_average = 0
    long_moving_average = 0
    while True:
        new_data = pipe.recv()
        if new_data:
            trade_holder.append(new_data)
            curr_data_received += 1
            if curr_data_received >= 10:
                find_moving_averages()
                end_time = dateutil.parser.parse(datetime.datetime.now(datetime.timezone.utc).isoformat())
                trade_time = dateutil.parser.parse(new_data["time"])
                print("Update took", (end_time-trade_time).microseconds, " microseconds")



TRADES_TO_GATHER = 10

#trade_holder = get_data(TRADES_TO_GATHER)
recv_pipe, send_pipe = Pipe(duplex=False)
data_process = Process(target = get_data, args = (TRADES_TO_GATHER, send_pipe))
math_process = Process(target = take_data_calc_ma, args = (TRADES_TO_GATHER, recv_pipe))

data_process.start()
math_process.start()
#signal_to_noise = get_data()

#print("the SNR is", signal_to_noise, "%")