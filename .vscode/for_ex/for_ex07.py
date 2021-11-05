year = 0
balance = 1000
while 2000 > balance : # while의 조건은 '참'인 경우에만 작된됩니다. 
    year = year + 1 
    interest = balance * 0.07
    balance = balance + interest

print(str(year)+'년이 결렸습니다.')

