a = []
a = list(map(int, input().split()))
tot = 0
for i in range(len(a)):
    tot = (-tot) - a[i]
print(tot)
