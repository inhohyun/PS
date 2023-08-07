from sys import stdin
from collections import deque   # deque 사용 연습 겸
n,m=map(int,stdin.readline().rstrip().split())
arr=[[0]*m for _ in range(n)]

for i in range(n):
    s=stdin.readline().rstrip()

    for j in range(m):
        arr[i][j]=int(s[j])

dx=[1,0,-1,0]
dy=[0,1,0,-1]
i=j=0
next=deque()
visit=[[0]*m for _ in range(n)]

next.append((i,j))
visit[i][j]=1
while len(next):
    now=next.popleft()
    i=now[0]
    j=now[1]

    for a in range(4):
        ddx=i+dx[a]
        ddy=j+dy[a]

        if ddx==-1 or ddx==n or ddy==-1 or ddy==m:
            continue
        if arr[ddx][ddy]==1 and visit[ddx][ddy]<=0:
            next.append((ddx,ddy))
            visit[ddx][ddy]=visit[i][j]+1

print(visit[n-1][m-1])