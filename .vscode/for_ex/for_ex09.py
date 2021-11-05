i = 0
j = 0
x = 0
for i in range(3,101,2):
    j = i + 2

    x += (i / j)
    print(int(x))