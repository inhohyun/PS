from sys import stdin
n=int(stdin.readline().rstrip())
q=[]

for _ in range(n):
    s=stdin.readline().rstrip().split()

    if len(s)==1:
        if s[0]=='pop':
            if len(q)==0:
                print(-1)
            else:
                print(q.pop(0))
        elif s[0]=='front':
            if len(q)==0:
                print(-1)
            else:
                print(q[0])
        elif s[0]=='back':
            if len(q)==0:
                print(-1)
            else:
                print(q[-1])
        elif s[0]=='size':
            print(len(q))
        else:
            if len(q)==0:
                print(1)
            else:
                print(0)
    else:
        q.append(int(s[1]))