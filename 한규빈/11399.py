n=int(input())
arr=list(map(int,input().split()))
min=list()

arr.sort()
min.append(arr[0])
sum=arr[0]

for i in range(1,n):
    min.append(min[i-1]+arr[i])
    sum+=min[i]

print(sum)