import time
import sys

def factorial(n):
    response = 1

    while n > 1:
        response *= n
        n -= 1

    return response

def factorial_recursive(n):
    if n == 1:
        return 1

    return n * factorial_recursive(n - 1)


if __name__ == '__main__':
    n = 2500
    sys.setrecursionlimit(n + 10)

    starting_time = time.time()
    factorial(n)
    end_time = time.time()
    print(f"Execution time with bucle\t{end_time - starting_time}")

    startin_time = time.time()
    factorial_recursive(n)
    end_time = time.time()
    print(f"Execution time with recusive\t{end_time - starting_time}")