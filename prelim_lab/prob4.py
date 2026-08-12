n = int(input("Please enter a number: "))
steps = 0
peak = n
x = n
while x !=1:
    if x % 2 == 0:
        x = x // 2
    else:
        x = 3 * x + 1
    if x > peak:
        peak = x
    steps += 1
print("Steps:", steps, ", Peak:", peak)
