# 백준 2822

import sys
input = sys.stdin.readline

arr = []
sum = 0
arrs = []

for i in range(8):
    n = int(input().strip())
    arr.append(n)
    



for i in range(5):
    
    sum += max(arr)
    arrs.append(arr.index(max(arr)) + 1)
    arr[arr.index(max(arr))] = -1

arrs.sort()

print(sum)
print(*arrs)


