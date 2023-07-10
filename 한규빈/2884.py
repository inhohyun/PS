h,m=map(int,input().split())

if m-45<0:
    h-=1
    if h<0:
        h+=24
    m+=-45+60
else:
    m-=45

print(h,m)