def guess_the_number(number):
    hidden = 37
    if number > hidden:
        return ("Too high")
    elif number < hidden:
        return ("Too low")
    else:
        return ("You got it!")

print(guess_the_number(55))
print(guess_the_number(99))
print(guess_the_number(24))
print(guess_the_number(37))
