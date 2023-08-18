from sys import stdin
t=int(stdin.readline().rstrip())

for _ in range(t):
    fibo=[0,1]
    z=[1,0]
    
    n=int(stdin.readline().rstrip())
    for i in range(2,n+1):
        fibo.append(fibo[i-1]+fibo[i-2])
        z.append(z[i-1]+z[i-2])
    print(z[n],fibo[n])