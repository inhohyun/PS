# n = int(input())

# T = []
# P = []
# for i in range(n):
#     a, b = map(int, input().split())
#     T.append(a)
#     P.append(b)
# total = 0
# def dfs(depth, n, temp):
#     global total
#     if depth == n:
#         total = max(temp, total)
#         return
#     if depth > n:
#         return
#     # 상담을 하는 경우
#     dfs(depth+T[depth], n, temp+P[depth])
#     # 상담을 안하는 경우
#     dfs(depth+1, n, temp)


# dfs(0,n,0)
# print(total)

# 다른 방식으로 풀어보자 -> DP? -> 아...오,....
N = int(input())

T = []
P = []
for i in range(N):
    a, b = map(int, input().split())
    T.append(a)
    P.append(b)

dp = [0] * (N+1)

for n in range(N-1, -1, -1): # 뒤에서 앞으로(완료 기준)
    if n+T[n] <= N: # 기간내 상담이 가능하다면
        dp[n] = max(dp[n+1], dp[n+T[n]] + P[n])
    else:
        dp[n] = dp[n+1]


print(dp[0])
