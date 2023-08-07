from sys import stdin
n=int(stdin.readline().rstrip())
m=int(stdin.readline().rstrip())
arr=[[0]*n for _ in range(n)]

for _ in range(m):
    a,b=map(int,stdin.readline().rstrip().split())
    a-=1
    b-=1
    arr[a][b]=arr[b][a]=1

visit=[0 for _ in range(n)]
visit[0]=1
next=[]
i=0
cnt=0
while True:
    for j in range(n):
        if visit[j]==0 and arr[i][j]==1:
            cnt+=1
            visit[j]=1
            next.append(j)
    
    if len(next)==0:
        break
    else:
        i=next.pop()

print(cnt)