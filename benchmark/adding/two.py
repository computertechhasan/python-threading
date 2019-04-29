from multiprocessing import Process
from multiprocessing import current_process
from multiprocessing import Pool
import os
import datetime
import dateutil.parser


def add_numbers(start, end):
    curr_sum = 0
    #start_time = datetime.datetime.now()
    for i in range(start, end):
        curr_sum += i
    print(curr_sum)
    #end_time = datetime.datetime.now()
    #return end_time - start_time

NUMS_TO_ADD = 100000000
PROCS_TO_RUN = 2
ends = []
for i in range(0, PROCS_TO_RUN):
    if i == 0:
        ends.append((i, NUMS_TO_ADD // PROCS_TO_RUN))
        continue
    else:
        ends.append((ends[i-1][1] + 1, ends[i-1][1]+ 1 + NUMS_TO_ADD // PROCS_TO_RUN))
start_time = datetime.datetime.now()
process_pool = Pool(PROCS_TO_RUN)
result = process_pool.starmap(add_numbers, ends)

process_pool.close()
process_pool.join()

end_time = datetime.datetime.now()
run_time = end_time - start_time
print("Two CPUs took", run_time, "to add", NUMS_TO_ADD, "numbers")

