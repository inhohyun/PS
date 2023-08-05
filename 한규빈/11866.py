from sys import stdin

n,k=map(int,stdin.readline().rstrip().split())
arr=[]
sarr=set()
i=k
cnt=k

while True:
    if i>n:
        i-=n

    if i in sarr:
        i+=1
        continue
    elif cnt%k==0:
        arr.append(i)
        sarr.add(i)

    i+=1
    cnt+=1
    if len(arr)==n:
        break

print("<",end="")
for i in range(n):
    print(arr[i],end="")
    if i<n-1:
        print(", ",end="")
print(">")