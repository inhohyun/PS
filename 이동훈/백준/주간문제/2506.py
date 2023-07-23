# 백준 2506 점수계산 브론즈 3

import sys

n = int(sys.stdin.readline())

m = list(map(int, sys.stdin.readline().split()))

sum = 0
value = 0



# i는 배열의 값들을 가져와준다
for i in m:
    if i == 0:
        sum = 0

    elif i == 1:
        sum += 1
        value += sum

print(value)