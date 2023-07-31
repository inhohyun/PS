from sys import stdin
n,m=map(int,stdin.readline().rstrip().split())
arr=list(map(int,stdin.readline().rstrip().split()))
sarr=[]
sarr.append(arr[0])

for i in range(1,n):
    sarr.append(sarr[i-1]+arr[i])

for i in range(m):
    a,b=map(int,stdin.readline().rstrip().split())
    print(sarr[b-1]-sarr[a-1]+arr[a-1])
