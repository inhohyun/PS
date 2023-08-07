from sys import stdin
n=int(stdin.readline().rstrip())
narr=set(map(int,stdin.readline().rstrip().split()))

m=int(stdin.readline().rstrip())
marr=list(map(int,stdin.readline().rstrip().split()))

for i in range(m):
    if marr[i] in narr:
        print(1,end=" ")
    else:
        print(0,end=" ")