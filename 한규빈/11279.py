from sys import stdin
from queue import PriorityQueue
n=int(stdin.readline().rstrip())
q=PriorityQueue()

for _ in range(n):
    i=int(stdin.readline().rstrip())

    if i==0:
        if q.qsize():
            print(q.get()*(-1))
        else:
            print("0")
    else:
        q.put(-i)
