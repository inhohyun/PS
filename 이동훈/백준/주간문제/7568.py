# 백준 7568 덩치

n = int(input())

arr = []
check = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x,y))



for i in range(n):
    count = 0
    for j in range(n):
        # print(i[0], j[0])
        # print(i[1], j[1])
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            count+=1
    check.append(count+1)

for k in check:
    print(k)
            
  