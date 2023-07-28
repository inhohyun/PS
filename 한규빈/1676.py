n=int(input())
p=1

for i in range(2,n+1):
    p*=i
res=str(p).split('0')

count=0
a=1
while True:
    if res=="" or not res[-a]=='':
        break
    
    count+=1
    a+=1

print(count)