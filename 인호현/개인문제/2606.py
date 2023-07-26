node = int(input())
edge = int(input())
# 그래프 초기화
graph = [[] for _ in range(node+1)]
# 방문한 컴퓨터 체크
visited = [0] * (node+1)

for i in range(edge):
    a,b = map(int, input().split())
    graph[a]+=[b] # a에 b 연결
    graph[b]+=[a] # b에 a 연결 -> 양방향
def dfs(edge):
    visited[edge] = 1
    for nx in graph[edge]:
        if visited[nx] == 0:
            dfs(nx)

dfs(1)
print(sum(visited)-1)

                 

