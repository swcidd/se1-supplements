##Problem 6 (Hard - Math & Loops)

##The Collatz sequence (also known as the Hailstone sequence) is generated for a starting positive integer x using these two math rules:
##* If x is even: divide it by 2 (x = x // 2)
##* If x is odd: multiply it by 3 and add 1 (x = 3x + 1)
##* Repeat this process until x reaches 1.
##Write a program that takes an integer n (n >= 1) as input and finds which starting number k (where 1 <= k <= n) generates the longest sequence (most steps to reach 1).
##Assign the output values to variables named longest_start and max_steps.
### Constraints:
##1. You must use a for loop to iterate through each starting candidate number k from 1 up to n.
##2. You must use a while loop to compute the Collatz sequence step count for each candidate number until it collapses to 1.
##3. Do not use external libraries or recursion.

n = int(input("Enter n:"))
longest_start = 1
max_steps = 0
for i in range(1, n + 1):
    current = i
    steps = 0

    while current != 1:
        if current % 2 == 0:
            current = current // 2
        else:
            current = 3 * current + 1
        steps = steps + 1

    if steps > max_steps:
        max_steps = steps
        longest_start = i
print("Starting number with longest sequence:", longest_start)
print("Number of steps", max_steps)


n = 5
for i in range(n):
    print('*'*n)