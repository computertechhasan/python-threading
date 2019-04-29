from websocket import create_connection
import json, timeit
from collections import deque
import datetime
import dateutil.parser

trade_holder = deque(maxlen = 10)

data_socket = create_connection("wss://ws-feed.pro.coinbase.com")
subscribe_message = {
    "type": "subscribe",
    "product_ids": [
        "BTC-USD"
    ]
}

SHORT_MA_LENGTH = 5
LONG_MA_LENGTH = 10

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

data_socket.send(json.dumps(subscribe_message))
message_count = 0
long = 10
while True:
    websocket_response = json.loads(data_socket.recv())
    if websocket_response["type"] == "match":
        message_count += 1
        trade_holder.append(websocket_response)
        if message_count >= long:
            find_moving_averages()
            end_time = dateutil.parser.parse(datetime.datetime.now(datetime.timezone.utc).isoformat())
            trade_time = dateutil.parser.parse(websocket_response["time"])
            print("Update took", (end_time-trade_time).microseconds, " microseconds")