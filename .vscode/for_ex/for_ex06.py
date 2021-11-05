x = 0
y = 0
for i in range(9):
    x += 1
    for j in range(9):
        y += 1
        print(x * y, end=' ')
    y = 0
    print('\n')