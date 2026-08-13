##Write a program that asks the user to enter numbers repeatedly. Use a while loop to continue asking until the user enters 0##

total = 0
number = int(input("Enter a number:"))
while number != 0:
    total = total + number
    number = int(input("Enter a number:"))
print("Total sum:",total)