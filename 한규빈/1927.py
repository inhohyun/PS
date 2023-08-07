from sys import stdin
from queue import PriorityQueue
n=int(stdin.readline().rstrip())
# 원래 set을 사용하여 구현하려고 했었는데, 만약, 데이터 중에서 중복 값이 있는 경우, 중복 값이 제거되어서는 안되므로 정답으로 인정되지 않을 가능성을 고려하여 사용하지 않음.
# l=set()

# 우선순위 큐 객체 생성
q=PriorityQueue()

for _ in range(n):
    i=int(stdin.readline().rstrip())

    if i==0:
        if q.qsize()>0:
            print(q.get())
        else:
            print("0")
    else:
        q.put(i)