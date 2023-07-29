from sys import stdin
k,n=map(int,stdin.readline().rstrip().split())
max=0
arr=[]

for _ in range(k):
    a=int(stdin.readline().rstrip())
    arr.append(a)

    if a>max:
        max=a

l=1
r=max
while l<=r:
    count=0
    m=(l+r)//2
    
    for i in range(k):
        count+=arr[i]//m

    if count<n:
        r=m-1
    else:
        l=m+1

print(r)