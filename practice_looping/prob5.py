##Problem 1: Right-Angled Number Pyramid (Easy)
##Write a Python program that takes an integer N and prints a right-angled triangle where row i
#contains the number i repeated i times.
#Input: N = 5

n = int(input("Enter a number:"))
for n in range(1, n + 1):
    for i in range(1, n):
        print(n, end=" ")
    print(n)