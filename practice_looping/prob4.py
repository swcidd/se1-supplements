string = input("Enter a string: ")
compressed_string = ""
count = 1

for i in range (len(string)):
    if i + 1 < (len(string)) and string[i] == string[i + 1]:
        count += 1
    else:
        compressed_string += string[i] + str(count)
        count = 1

print(compressed_string)