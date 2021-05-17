def caching_fibonacci():
    cache = {0: 0, 1: 1}

    def fibonacci(n):

        for k in range(2, n+1):
            if k not in cache:
                cache[k] = cache[k-1] + cache[k-2]

        return cache[k]

        # return cache.setdefault(n, fibonacci(n-2) + fibonacci(n-1))

    return fibonacci


print(caching_fibonacci()(7))
