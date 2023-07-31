# 백준 2960 에라토스테네스의 체 실버4
import sys

n, k = map(int, sys.stdin.readline().split())

arr = [False] * (n+1)
count = 0

for i in range(2, n+1):
    if arr[i] == False:
        for j in range(i, n+1, i):
            if arr[j] == False:
                arr[j] = True
                count += 1
                if count == k:
                    print(j)

        
        
        

    
        