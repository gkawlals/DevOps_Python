import random 


x = random.randint(1, 9)
y = random.randint(1, 9)

cur = '+-/*'
i = random.choice(cur)

if i == '+' :
    tot = int(input(str(x) + ' + ' + str(y) + '의 값은? :'))
    if (x + y) == tot:
        print('정답입니다.')
    else : 
        print('틀렸습니다.')
if i == '*':
    tot = int(input(str(x) + ' * ' + str(y) + '의 값은? :'))
    if (x * y) == tot:
        print('정답입니다.')
    else : 
        print('틀렸습니다.')
if i == '/':
    tot = int(input(str(x) + ' / ' + str(y) + '의 값은? :'))  
    if (x / y) == tot:
        print('정답입니다.')
    else : 
        print('틀렸습니다.')
if i == '-':
    tot = int(input(str(x) + ' - ' + str(y) + '의 값은? :'))  
    if (x - y) == tot:
        print('정답입니다.')
    else : 
        print('틀렸습니다.')
