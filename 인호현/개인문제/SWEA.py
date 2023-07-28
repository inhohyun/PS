T = int(input())
for a in range(1, T+1):
    # N : 재료 개수, L : 제한 칼로리
    N, L = map(int, input().split())
    ham = []
    # 맛의 합
    sum_tast = 0
    sum_cal = 0
    for i in range(N):
        (x, y) = map(int, input().split())
        ham.append((x, y))
        # 재료별 칼로리 기준으로 정렬
        sorted_ham = sorted(ham, key=lambda x : x[1])
    
    # 재귀로 돌려야할듯?


# 개수, 제한 칼로리를 이용해 모든 경우의 수 구하기
def dfs(sorted_ham, N, L, sum_tast, sum_cal):
    if sum_cal > L:
        return
    

