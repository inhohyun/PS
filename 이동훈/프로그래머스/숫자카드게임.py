# 코딩테스트 책 그리디
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
min = 99999
max = 0
for i in range(n):
        x = list(map(int, input().split()))
        x.sort()
        
        
        arr.append(x[0])
        


for j in range(len(arr)):
        if max < arr[j]:
                max = arr[j]
          



print(arr)
print(max)