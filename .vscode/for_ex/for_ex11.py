from random import randint as rd

print('실행결과')
for i in range(10):
    x = rd(1,6)  # 첫번째 주사위
    y = rd(1,6)  # 두번째 주사위
    print('첫번째 주사위 : ',x,'두번째 주사위 : ',y)