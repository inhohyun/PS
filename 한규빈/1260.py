# n=정점 수, m=간선 수, v=시작점
n,m,v=map(int,input().split())
# 정점에 연결되는 간선을 넣을 이중 리스트(배열)
node=[[0]*n for _ in range(n)]
# 각 DFS, BFS 결과를 넣을 리스트
dfs=[]
bfs=[]

# 간선을 입력 받음
for _ in range(m):
    a,b=map(int,input().split())
    # 해당 문제는 무방향(양방향) 그래프이므로, 양쪽 간선 배열에 모두 연결되었음을 표시해야 함.
    node[a-1][b-1]=node[b-1][a-1]=1

# - DFS 구현
# 방문 여부를 담을 리스트를 모두 0으로 초기화
visit=[0 for _ in range(n)]
# 재귀를 이용하여 구현하기 위해 함수 선언
def dfs_fun(now):
    # 방문한 정점을 리스트에 추가하고, 방문 여부를 표시
    dfs.append(now+1)
    visit[now]=1
    # 다음 정점 방문을 위해 반복
    for i in range(n):
        # 만약, 연결된 간선 중에 아직 방문하지 않은 정점이 있는 경우, 해당 정점을 방문하기 위해 재귀 실행
        if node[now][i]==1 and visit[i]==0:
            dfs_fun(i)

# DFS 탐색 시작점을 정의
start=v-1
# DFS 재귀 탐색 함수 호출
dfs_fun(start)

# - BFS 구현
# 첫 방문할 시작점을 정의
now=v-1
# 방문 여부를 담을 리스트를 0으로 초기화
visit=[0 for _ in range(n)]
# 현재 방문한 위치는 이미 방문한 것으로 함.
visit[now]=1
# 방문할 정점을 담을 리스트 변수 선언(큐 형태로 사용)
queue=[]
# 현재 방문한 위치는 큐에 추가
queue.append(now)

# BFS 탐색 시작
while len(queue)>0:
    # 현재 탐색 위치는 큐에서 빼오고, 방문한 정점 추가
    now=queue.pop(0)
    bfs.append(now+1)

    # 다음 방문 위치를 큐에 추가하기 위해 반복
    for i in range(n):
        # 간선이 연결되어있지만, 아직 방문하지 않은 정점은 큐에 추가하여 다음에 방문할 수 있도록 함.
        if node[now][i]==1 and visit[i]==0:
            visit[i]=1
            queue.append(i)

# 결과 출력 (DFS, BFS 순)
for i in range(len(dfs)):
    print(dfs[i],end=" ")
print() # 줄바꿈을 위한 빈 print 함수 실행

for i in range(len(bfs)):
    print(bfs[i],end=" ")