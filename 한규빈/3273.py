import sys
n=int(sys.stdin.readline().rstrip())
arr=list(map(int,sys.stdin.readline().rstrip().split()))
x=int(sys.stdin.readline().rstrip())

count=0
start=0
end=n-1
arr.sort()

while True:
    if start==end:
        break
    
    res=arr[start]+arr[end]
    if res==x:
        count+=1
        end-=1
    elif res>x:
        end-=1
    else:
        start+=1

print(count)