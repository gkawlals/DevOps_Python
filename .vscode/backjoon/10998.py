a = list(map(int, input().split()))
tot = 1
for i in range(len(a)):
    tot = tot * a[i]
    
print(tot)
