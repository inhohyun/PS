from sys import stdin
t=int(stdin.readline().rstrip())

for _ in range(t):
    n,m=map(int,stdin.readline().rstrip().split())
    tarr=list(map(int,stdin.readline().rstrip().split()))
    arr=[]
    q=[]

    for i in range(n):
        arr.append((tarr[i],i))
        q.append(arr[i])
    
    arr.sort(key=lambda x:-x[0])

    i=0
    cnt=0
    next=arr.pop(0)
    while True:
        now=q.pop(0)

        if now[0]==next[0]:
            if len(arr)>0:
                next=arr.pop(0)
            cnt+=1
        else:
            q.append(now)
            continue
        
        if now[1]==m:
            break
    
    print(cnt)