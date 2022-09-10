import time

def calculate(function, result=False):
    start_time = time.time()
    result = function()
    end_time = time.time()
    the_return = end_time - start_time
    if result:
        return the_return, result
    return the_return