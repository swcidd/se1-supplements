#sum from 1 to N
def sum_of_n (n):
    total_sum = 0
    for i in range (1, n + 1):
        total_sum += i
    return total_sum  
print(sum_of_n(5))   # 15
print(sum_of_n(10))  # 55

#Factorial
#Compute the factorial of a positive interger. Example:5! = 5 x 4 x 3 x 2 x 1 = 120.
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Test
print(factorial(4))  # 120
print(factorial(0))  # 1

#Reverse a number
#reverse the digits of a positive integer without converting it to a string


def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10          # get last digit
        reversed_num = reversed_num * 10 + digit
        num //= 10                # remove last digit
    return reversed_num

# Example
print(reverse_number(12345))  # 54321
print(reverse_number(9870))   # 789

