import sys
n,m=map(int,sys.stdin.readline().rstrip().split())
dic1=dict()
dic2=dict()

for i in range(1,n+1):
    dic1[i]=sys.stdin.readline().rstrip()
    dic2[dic1[i]]=i

for _ in range(m):
    s=sys.stdin.readline().rstrip()
    try:
        print(dic1.get(int(s)))
    except:
        print(dic2.get(s))