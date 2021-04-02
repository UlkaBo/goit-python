import sys


def main():
    n = int(sys.argv[1])
    print(fibonacci(n))


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    print(main())
