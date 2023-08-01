# 백준 2110 공유기 설치

import sys

input = sys.stdin.readline
arr = []



n, c = map(int, input().split())

start = 0
end = n-1

for i in range(n):
    x = int(input())
    arr.append(x)
    
def check(arr, num):
    
    mid = (start + end) // 2

    value_1 = arr[mid] - arr[start]
    value_2 = arr[end] - arr[mid]
    if value_1 > value_2 :
        value = value_1
    else:
        value = value_2




arr.sort()
print(arr)
print(value)


