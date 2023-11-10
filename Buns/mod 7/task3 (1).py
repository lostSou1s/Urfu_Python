import time


def memoize(func):
    cache = {}

    def inner(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]

    inner.__name__ = func.__name__
    inner.__doc__ = func.__doc__

    return inner


def timer(func):
    def wrapper(*args):
        start_time = time.time()
        result = func(*args)
        end_time = time.time()
        execution_time = end_time - start_time
        return (f"{func.__name__}: "
                f"argument: {args[0]} "
                f"time: {execution_time}")

    return wrapper


@timer
@memoize
def fibonacci_memoize(n):
    """
    with memoize
    :param n = fibonacci sequence element:
    :return current element:
    """
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@timer
def fibonacci(n):
    """
    :param n = fibonacci sequence element:
    :return current element:
    """
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci_memoize(30))
print()
print(fibonacci(30))
