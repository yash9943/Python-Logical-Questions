'''
 Q10. Decorator for Function Execution Time (10 Marks)
 Write a decorator that measures how long a function takes to execute.
'''
import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Exectution time for {func.__name__} : {execution_time:.8f} seconds")
        return result,
    return wrapper

@timeit
def printit():
    print("Function executed")
    
printit()
