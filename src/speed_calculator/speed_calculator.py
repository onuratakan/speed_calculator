import time

def calculate(function, *args, result=False):
    start_time = time.time()
    result = function(*args)
    end_time = time.time()
    the_return = end_time - start_time
    if result:
        return the_return, result
    return the_return