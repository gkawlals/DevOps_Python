hight = float(input('키(M 단위) 는?'))
weight = int(input('몸무게는? 는?'))

BMI = weight // hight

if BMI < 25:
    print('정상')
elif BMI <= 29.9:
    print('과체중')
elif BMI > 30 :
    print('비만입니다.')

print(BMI)