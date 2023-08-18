from sys import stdin
n=int(stdin.readline().rstrip())
stack=[]

for _ in range(n):
    s=stdin.readline().rstrip().split()

    if len(s)==1:
        if s[0]=='pop':
            if len(stack)==0:
                print(-1)
            else:
                print(stack.pop())
        elif s[0]=='top':
            if len(stack)==0:
                print(-1)
            else:
                print(stack[-1])
        elif s[0]=='size':
            print(len(stack))
        else:
            if len(stack)==0:
                print(1)
            else:
                print(0)
    else:
        stack.append(int(s[1]))