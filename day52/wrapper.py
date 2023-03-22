import time
current_time = time.time()
# print(current_time)

def speed_calc_decorator(function):
    current_time = time.time()
    function()
    print(f"{function.__name__} run speed: {time.time()-current_time}")

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i
    

@speed_calc_decorator        
def slow_function():
    for i in range(100000000):
        i * i
    
