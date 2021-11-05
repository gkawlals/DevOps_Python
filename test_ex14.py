import random 



x = random.randint(10,99)

print(x)

num1 = x // 10
num2 = x % 10
print(num1, num2 )

lo = int(input('복권번호를 10 ~ 99사이의 번호값으로 입력해주세요'))

if num1 == (lo // 10) or num2 == (lo % 10):
    print('축하합니다 50만원 당첨')
    if num1 == (lo // 10) and num2 == (lo % 10):
        print('축하합니다. 100만원 당첨')
else :
    print('실패')





