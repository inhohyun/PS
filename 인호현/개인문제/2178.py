from collections import deque
N,M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, list(input()))))

# queue를 이용한 bfs로 탐색해보기

def bfs(si,sj):
    q = deque()
    # 시작점 저장
    q.append((si,sj))
    
    cnt = 0
    while q:
        hi,hj = q.popleft()

        for ni,nj in ((1,0),(-1,0), (0,1), (0,-1)):
            di = hi+ni
            dj = hj+nj
            if di <0 or dj <0 or di > N-1 or dj > M-1:
                continue

            if graph[di][dj] == 1:
                cnt += 1
                q.append((di,dj))
                graph[di][dj] = graph[hi][hj] + 1
    return graph[N-1][M-1]


print(bfs(0,0))
