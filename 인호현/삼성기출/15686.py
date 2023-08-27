# n, m = map(int, input().split())

# arr = []
# for _ in range(n):
#     arr.append(list(map(int, input().split())))

# answer = []

# # 집 위치를 기반으로 해당집과 가장 가까운 치킨거리를 세는 함수
# def countChiken(x,y):
#     global arr
#     chickenRoad = 1e9
#     for ci in range(n):
#         for cj in range(n):
#             if arr[ci][cj] == 2:

#                 chickenRoad = min(chickenRoad, abs(ci-x) + abs(cj -y))
    
#     return chickenRoad




# # 치킨집을 m개 말고 전부 제거하는 함수
# def lostChiken(current_chiken):
#     global answer, arr
#     if current_chiken == m:
#         for ci in range(n):
#             for cj in range(n):
#                 if arr[ci][cj] ==1 and not visited[ci][cj]:
#                     visited[ci][cj] = True
#                     answer.append(countChiken(ci,cj))
                    
                    
#         return
    
    
#     for i in range(n):
#         for j in range(n):
#             if arr[i][j] == 2:
                
#                 arr[i][j] = 0
#                 lostChiken(current_chiken - 1)
#                 arr[i][j] = 2
                

# visited = [[False] * n for _ in range(n)]  
# cnt = 0
# for i in range(n):
#     for j in range(n):
#         if arr[i][j] == 2:
#             cnt += 1


# lostChiken(cnt)
# print(answer)
# print(sum(answer))

# 위의 코드 에러잡기
def cal(tList):
    #모든 집과 tList의 치킨집거리 중 최소값의 누적값 구하기
    sm = 0
    for hi,hj in home: # 집 좌표를 하나씩 처리(최소값 구하기)
        mn = 2 *n
        for ci, cj in tList:
            mn = min(mn, abs(hi-ci)+abs(hj-cj))
        # 도시의 치킨거리 끝내기
        sm += mn

    return sm


def dfs(N, tList):
    global ans
    if N == cnt:
        if len(tList) == m:
            ans = min(ans, cal(tList))
        
        return
    dfs(N+1, tList + [chicken[N]]) # 유지하는 경우
    dfs(N+1, tList) # 폐업하는 경우



n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 1. 집, 치킨집 좌표를 home, chicken에 저장
home = []
chicken = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            home.append((i,j))
        elif arr[i][j] == 2:
            chicken.append((i,j))

cnt = len(chicken)

ans = 1e9
dfs(0, [])
print(ans)


