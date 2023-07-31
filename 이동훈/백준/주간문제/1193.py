# 백준 1193
# 다시풀기
import sys
input = sys.stdin.readline
n = int(input())

arr = [True] * (n+1)
arrs = []
count = 0

for i in range(1, n+1):
    
    for j in range(1, n+1):
        if arr[j] == True:
            arr[j] == False
            count += 1
            print(j,"/", i)

            if count == n:
                print(i,"/", j)

        else:
            continue 
        
# print(count)
