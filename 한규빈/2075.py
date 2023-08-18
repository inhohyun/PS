from sys import stdin
import heapq
n=int(stdin.readline().rstrip())
hq=[]

for _ in range(n):
    a=list(map(int,stdin.readline().rstrip().split()))

    for i in a:
        if len(hq)<=n or i>hq[0]:
            heapq.heappush(hq,i)
            if len(hq)>n:
                heapq.heappop(hq)

print(heapq.heappop(hq))