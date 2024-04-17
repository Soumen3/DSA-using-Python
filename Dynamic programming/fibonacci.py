def fibonacci(n):
    # Create a memoization table to store computed Fibonacci numbers
    memo = {}

    # Base cases
    if n <= 1:
        return n

    # Check if the result is already memoized
    if n in memo:
        return memo[n]

    # If not memoized, calculate and store the result
    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]

# Example usage:
n = 10
print(f"Fibonacci({n}) = {fibonacci(n)}")
