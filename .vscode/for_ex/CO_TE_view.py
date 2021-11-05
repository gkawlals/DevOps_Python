
for j in range(1, 11):
    r = int(input())
    T = list(map(int, input().split()))
    c = 0
    for i in range(2, r-2):
        #왼쪽과 오른쪽 빌딩중에서 제일 빌딩을 찾음
        m = max(T[i+1], T[i+2], T[i-1], T[i-2])
        # 현재 빌딩과 제일큰빌딩을 비교할때 현재빌딩보다 작다면 차 만큼 결과에 더해주기
        if T[i] - m > 0 :
            c += T[i] - m
    print("#{} {}".format(j, c))