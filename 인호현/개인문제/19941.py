n, k = map(int, input().split())
ham = list(input())
cnt = 0
# 각각의 원소를 비교하여 이중 for문으로 먹을 수 있는 햄버거 찾기
for i in range(n):
    # 사람일 경우
    if ham[i] == 'P':
        for j in range(i-k, i+k+1):

            if 0<= j < n and ham[j] == 'H':
                ham[j] = 0
                cnt += 1
                break
    

print(cnt)
            

# 전근법은 맞았는데? -> 구현력 부족