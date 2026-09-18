#A farmer is tracking rabbit population growth. Rabbits reproduce following the Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8.... He wants to know how many rabbits there will be in the nth month.
#👉 Write a function that returns the nth Fibonacci number.

def nth_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0,1
    for i in range (2 , n + 1):
        a, b = b, a + b
    return(b)
print(nth_fibonacci(6))