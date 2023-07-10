h,m=map(int,input().split())
w=int(input())

m+=w
if m>=60:
    wh=int(m/60)
    h+=wh
    if h>23:
        h-=24
    m-=wh*60

print(h,m)