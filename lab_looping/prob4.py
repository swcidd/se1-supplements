text = input("Enter a string: ")
new_string = "" 
for char in text:
    if char != " ":
        new_string += char
print(new_string)