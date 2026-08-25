##Write a function named is_prime(n) that takes a positive integer n. It should return True if n is a prime number and False otherwise. A prime number is greater than 1 and has no positive divisors other than 1 and itself.
def is_prime(n):
    if n == 1:
        return False
    if n % 2 == 0 or n % 3 == 0:
        return False
    return True

print(is_prime(7))   # Expected output: True
print(is_prime(10))  # Expected output: False
print(is_prime(1))   # Expected output: False   
