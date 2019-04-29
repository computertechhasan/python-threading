from multiprocessing import Process
from multiprocessing import current_process
import os
import time

def first():
    my_pid = os.getpid()
    my_ppid = os.getppid()
    print(my_pid)
    print("HI", my_pid)
    print("my mom is", my_ppid)
    time.sleep(30)
    
def second():
    my_pid = os.getpid()
    my_ppid = os.getppid()
    print("yo fam", my_pid)
    print("my dad is", my_ppid)
    time.sleep(30)
    
my_processes = []

first_process = Process(target = first, args = ())
my_processes.append(first_process)
second_process = Process(target = second, args = ())
my_processes.append(second_process)

for process in my_processes:
    process.start()