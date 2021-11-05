i = 87
j = 36 

tot = i + j 

while True:
    anser = int(input(str(i) + '+' + str(j) + '의 답은?'))
    if tot == anser:
        print('정답')
        break
    else : 
        print('틀렸으')