import time

def calculate(function):
    start_time = time.time()
    function()
    end_time = time.time()
    return end_time - start_time