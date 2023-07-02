n = int(input())
T = []
P = []
for _ in range(n):
    time, money = map(int, input().split())
    T.append(time)
    P.append(money)
ans = []
def dfs(depth, money):
    if depth == n:
        ans.append(money)
        return
    
    # 회의 시간을 넘어간 경우
    if depth > n:
        return 

    # 상담을 하는 경우
    dfs(depth+T[depth], money+P[depth])
    # 상담을 안하는 경우
    dfs(depth+1, money)

dfs(0,0)
print(max(ans))