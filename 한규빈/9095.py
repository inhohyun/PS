from sys import stdin
n=int(stdin.readline().rstrip())

for _ in range(n):
    arr=[1,2,4]
    i=int(stdin.readline().rstrip())-1

    for j in range(3,i+1):
        arr.append(arr[j-3]+arr[j-2]+arr[j-1])
    
    print(arr[i])
