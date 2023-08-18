from sys import stdin
n=int(stdin.readline().rstrip())
a=set(map(int,stdin.readline().rstrip().split()))

m=int(stdin.readline().rstrip())
b=list(map(int,stdin.readline().rstrip().split()))

for i in range(m):
    if b[i] in a:
        print(1)
    else:
        print(0)