text = input("Enter a string: ")
new_string = ""
vowels = "aeiou"
for char in text:
    if char .lower() in vowels:
        new_string += "*" 
    else:
        new_string += char
print(new_string)