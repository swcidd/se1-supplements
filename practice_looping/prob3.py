##Create a program that asks the user for a number and displays its multiplication table from 1 to 10 using a for loop.##
##Then, ask the user if they want to try another number. Use a while loop to repeat the program until they answer "no" ##

answer = "yes"

while answer == "yes":
    number = int(input("Enter a number:"))
    for i in range (1, 11):
        print(number, "x", i, "=", number * i)
    answer = input("You want to try another number?")