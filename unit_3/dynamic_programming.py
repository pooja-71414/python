def fibonacci(n):
    # Create a table to store Fibonacci numbers
    fib_table = [0] * (n + 1)
    # Base cases
    fib_table[0] = 0
    fib_table[1] = 1
    
    # Fill the table
    for i in range(2, n + 1):
        fib_table[i] = fib_table[i - 1] + fib_table[i - 2]
    
    return fib_table[n]

# Example usage
print(fibonacci(10))  # Output: 55
