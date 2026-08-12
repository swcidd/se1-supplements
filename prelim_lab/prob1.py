start = int(input("Enter a starting number:"))
end = int(input("Enter an ending number:"))

total_even = 0

if start > end:
    print(0)
    
else:    
    for i in range (start, end + 1):
        if i % 2 == 0:
            total_even += i
    print(total_even)
