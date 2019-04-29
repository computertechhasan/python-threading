from multiprocessing import Process
from multiprocessing import current_process
import os
import datetime
import dateutil.parser


def add_numbers(start, end):
    curr_sum = 0
    start_time = datetime.datetime.now()
    for i in range(start, end):
        curr_sum += i
    end_time = datetime.datetime.now()
    print(curr_sum)
    return end_time - start_time

NUMS_TO_ADD = 100000000

run_time = add_numbers(0, NUMS_TO_ADD)
print("One CPU took", run_time, "to add", NUMS_TO_ADD, "numbers")