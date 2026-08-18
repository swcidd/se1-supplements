##Without using *(multiplication) operator##

rows = int(input("Enter number of rows: "))

rows = rows // 2 + 1

for i in range (1, rows + 1):
    spaces = rows - i

    line = ""

    for b in range(spaces):
        line += " "

    if i == 1:
        line += "*"
    else:
        line += "*"
        #and
        inner_spaces = i + i - 3

        for c in range(inner_spaces):
            line += " "

        else: 
            line += "*"

    print(line)


for i in range(rows - 1, 0, -1):
    spaces = rows - i

    line = ""

    for b in range(spaces):
        line += " "

    if i == 1:
        line += "*"

    else:
        line += "*"
        #and
        inner_spaces = i + i - 3
        for c in range(inner_spaces):
            line += " "

        else:
            line += "*"
    print(line)