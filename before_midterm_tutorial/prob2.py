#sum from 1 to N
n = int(input("Enter n:"))
total_sum = 0
for i in range (1, n + 1):
    total_sum += i
print("sum=",total_sum)

#Factorial
#Compute the factorial of a positive interger. Example:5! = 5 x 4 x 3 x 2 x 1 = 120.
num = int(input("Enter a number:"))
factorial = 1
for i in range (1 , num + 1):
    factorial *= i 
print(f"{num}!=", factorial)

#Reverse a number
#reverse the digits of a positive integer without converting it to a string

def reverse_number (n):
    while number > 0:
        digit = number % 10
        reverse_number = reversed_number * 10 + digit
        number = number // 10
        print(f"current reversed number {reverse}")
        print(f"number remaining {n}")
    print(reverse)
reverse_a_number(4321)