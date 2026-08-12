num = int(input("Please enter a number: "))
if num == 0:
    print(0)
else:
    while num >= 10:
        sum_digits = 0
        temp = num
        while temp > 0:
            sum_digits += temp % 10
            temp = temp // 10
        num = sum_digits
    print(num)

