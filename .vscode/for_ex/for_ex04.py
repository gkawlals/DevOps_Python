i = 0
cnt = 0
while True:
    j = int(input('입력할 숫자는?'))
    i = i + j

    j =0
    cnt += 1

    if cnt == 4:
        print('입력한 숫자들의 합 = ' + i)
        break
