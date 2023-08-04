from sys import stdin
t=int(stdin.readline().rstrip())

for i in range(t):
    n=int(stdin.readline().rstrip())
    arr=[1,1,1]
    for j in range(3,n):
        arr.append(arr[j-3]+arr[j-2])
    print(arr[n-1])