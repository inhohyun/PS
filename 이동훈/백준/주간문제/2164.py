# 백준 2164 카드2
from collections import deque
import sys
input = sys.stdin.readline

n = int(input().strip())
queue = deque()

for i in range(1,n+1):
    queue.append(i)



while len(queue) > 1:
    queue.popleft()
    
    queue.append(queue.popleft())

print(queue.pop())
