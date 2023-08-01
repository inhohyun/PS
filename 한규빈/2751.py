from sys import stdin
n=int(stdin.readline().rstrip())
arr=[]
for _ in range(n):
    arr.append(int(stdin.readline().rstrip()))

arr.sort()

for a in arr:
    print(a)