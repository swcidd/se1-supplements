s = input("Enter string:")
found = False
for char in s:
    count = 0
    for c in s:
        if c == char:
            count += 1
    if count == 1:
        print(char)
        found = True
        break
if found == False:
    print("_")
