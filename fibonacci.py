def fibonacci(n):
    if n <= 1:
        return n  # Base case: Fibonacci(0) = 0, Fibonacci(1) = 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
