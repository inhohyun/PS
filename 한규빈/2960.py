from sys import stdin
n,k=map(int,stdin.readline().rstrip().split())
arr=[False for i in range(n+1)]
cnt=[0,0,False]

for i in range(2,n+1):
    for j in range(i,n+1,i):
        if arr[j]==True:
            continue
        
        arr[j]=True
        cnt[0]+=1

        if cnt[0]==k:
            cnt[1]=j
            cnt[2]=True
            break
    if cnt[2]==True:
        break
    
print(cnt[1])