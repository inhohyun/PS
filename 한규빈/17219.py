import sys
n,m=map(int,sys.stdin.readline().rstrip().split())
acc=dict()

for _ in range(n):
    s1,s2=map(str,sys.stdin.readline().rstrip().split())
    acc[s1]=s2
for _ in range(m):
    s=sys.stdin.readline().rstrip()
    print(acc.get(s))