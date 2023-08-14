from sys import stdin
from collections import deque
n=int(stdin.readline().rstrip())
dq=deque()

for _ in range(n):
    s=stdin.readline().rstrip().split()

    if len(s)==1:
        if s[0]=='pop_front':
            if len(dq)==0:
                print(-1)
            else:
                print(dq.popleft())
        elif s[0]=='pop_back':
            if len(dq)==0:
                print(-1)
            else:
                print(dq.pop())
        elif s[0]=='front':
            if len(dq)==0:
                print(-1)
            else:
                print(dq[0])
        elif s[0]=='back':
            if len(dq)==0:
                print(-1)
            else:
                print(dq[-1])
        elif s[0]=='size':
            print(len(dq))
        else:
            if len(dq)==0:
                print(1)
            else:
                print(0)
    else:
        if s[0]=='push_front':
            dq.appendleft(int(s[1]))
        else:
            dq.append(int(s[1]))
            