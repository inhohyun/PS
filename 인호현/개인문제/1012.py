from collections import deque

dx = [0,0,1,-1]
dy = [1, -1, 0,0]

t = int(input())

# 주변에 1들을 모두 0으로 만드는 메서드
def bfs(graph, a, b):
    q = deque()
    q.append((a,b))
    graph[a][b] = 0

    # 근처에 1이 없을때까지 반복
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <0 or nx >= n or ny<0 or ny>= m:
                continue
            # 근처의 1들을 0으로 만들기
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                # 이동한 위치에서도 동서남북 검사하도록 큐에 추가
                q.append((nx, ny))
    return

for i in range(t):
    cnt = 0
    n, m, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]

    # 지렁이 위치 추가
    for j in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1
    
    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                # 주변 1들을 모두 0으로 만들기
                bfs(graph, a, b)
                cnt += 1

    print(cnt)            
