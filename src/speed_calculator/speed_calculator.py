import time

def calculate(function):
    start_time = time.time()
    function()
    end_time = time.time()
    return int(end_time - start_time)