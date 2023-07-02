# 1436번 평균

import sys

num = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().rstrip().split()))

# list에서 가장 큰 값을 가져오기
mx = max(data)
sum = 0


for i in range(num):
    
    data[i] = data[i] / mx * 100
    sum += data[i]

print(sum/num)

    