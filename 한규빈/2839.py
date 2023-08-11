from sys import stdin
n=int(stdin.readline().rstrip())
res=0

while n>0:
    if n%5==0:
        res+=n//5
        break
    n-=3
    res+=1

    if n==1 or n==2:
        res=-1
        break
    
print(res)