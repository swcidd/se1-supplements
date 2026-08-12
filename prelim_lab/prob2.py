N = int(input("Enter N: "))
current = N
while current >= 1:
    if current % 3 == 0 and current  % 5 == 0:
        print("FooBar", end=" ")
    elif current % 3 == 0:
        print("Foo", end=" ")
    elif current % 5 == 0:
        print("Bar", end=" ")
    else:
        print(current, end=" ")
    current -=1
