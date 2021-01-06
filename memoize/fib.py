import datetime

FIB_DICT = {}

def memo_fib(n):
    global FIB_DICT
    if n in FIB_DICT:
        return FIB_DICT[n]
    elif n == 1:
        FIB_DICT[n] = 0
        return 0
    elif n == 2:
        FIB_DICT[n] = 1
        return 1
    else:
        tmp = memo_fib(n-1) + memo_fib(n-2)
        FIB_DICT[n] = tmp
        return tmp

def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
        
if __name__ == "__main__":
    x = 999
    """
    print(fib(5))
    print(fib(8))
    start_time = datetime.datetime.now()
    print(fib(x))
    end_time = datetime.datetime.now()
    run_time = end_time - start_time
    print("One CPU took", run_time, "to find", x, " fibs")
    """
    start_time = datetime.datetime.now()
    print(memo_fib(x))
    end_time = datetime.datetime.now()
    run_time = end_time - start_time
    print("memo version took", run_time, "to find", x, " fibs")