s = input("Please enter a string: ")
if s == "":
    print()
else:
    result = ""
    current_char = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == current_char:
            count = count + 1
        else:
            result = result + current_char + str(count)
            current_char = s[i]
            count= 1
    result = result + current_char + str(count)
    print(result)
