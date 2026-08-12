n = int(input("Please enter an odd number: "))
mid = n // 2

for i in range(mid + 1):
    for j in range(n):
        if j == mid - i or j == mid + i:
           print("*", end="")
        else:
            print(" ", end="")
    print()
        
for i in range(mid - 1, -1, -1):
    for j in range(n):
        if j == mid - i or j == mid + i:
            print("*", end="")
        else:
           print(" ", end="")
    print()
