from sys import stdin
n=int(stdin.readline().rstrip())
arr=[]

for _ in range(n):
    age,name=map(str,stdin.readline().rstrip().split())
    arr.append([int(age),name])

arr.sort(key=lambda x:x[0])

for r in arr:
    print(r[0],r[1])
