def caching_fibonacci():
    cache = {0: 0, 1: 1}

    def fibonacci(n):

        if n in cache:
            return cache[n]
        cache[n] = fibonacci(n-2) + fibonacci(n-1)
        return cache[n]

        # return cache.setdefault(n, fibonacci(n-2) + fibonacci(n-1))

    return fibonacci


print(caching_fibonacci()(7))
