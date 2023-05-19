# Function decorater in Py
# https://github.com/gennad/Design-Patterns-in-Python/blob/master/decorator.py

import time

def time_this(func):
    """The time_this decorator"""

    def decorated(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print('Rain in', time.time() - start, 'seconds')
        return result
    return decorated

# Decorator syntax
# count = time_this(count)
@time_this
def count(until):
    """Counts to 'until', then returns the result"""

    print("Counting to", until, "…")
    num = 0
    time.sleep(1)
    for i in range(until):
        num += 1
    return num

# Run count with various values
for number in [10000, 100000, 1000000]:
    print(count(number))
    print("-" * 20)


# =============================================

# Decorator with parameters - Repeat decorators
# https://machinelearningmastery.com/a-gentle-introduction-to-decorators-in-python/

def repeat_decorator(num_repeats = 2):
    # repeat_decorator should return a function that's a decorator
    def inner_decorator(fn):
        def decorated_fn():
            for i in range(num_repeats):
                fn()
        # return the new function
        return decorated_fn
    # return the decorator that actually takes the function in as the input
    return inner_decorator

# use the decorator with num_repeats argument set as 5 to repeat the function call 5 times
@repeat_decorator(5)
def hello_world():
    print("Hello world!")

# call the function
hello_world()