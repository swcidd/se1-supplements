##Write a function named calculate_factorial(n) that takes a non-negative integer n and returns its factorial. The factorial of a number is the product of all positive integers less than or equal to n. The factorial of 0 is 1.

def calculate_factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(calculate_factorial(5))  # Expected output: 120
print(calculate_factorial(0))  # Expected output: 1
print(calculate_factorial(3))  # Expected output: 6