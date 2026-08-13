#Put your input logic here
string = input("Enter a string: ")
new_string = ""
vowels = "aeiou"
#Put your for loop logic here
for letter in string:

    if letter.lower() in "aeiou":
        new_string += "*"
    else:
        new_string += letter

print(f"{new_string} Kla")
print("Hello, {new_string}!")
print("Hello," + new_string)
print(new_string) 
