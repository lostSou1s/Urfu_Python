def memoize(func):
    cache = {}

    def inner(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]

    inner.__name__ = func.__name__
    inner.__doc__ = func.__doc__

    return inner


@memoize
def fibonacci(n):
    """
    :param n = fibonacci sequence element:
    :return current element:
    """
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))
