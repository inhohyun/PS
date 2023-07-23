# 백준 2455 지능형 기차 브론즈 3

import sys


value = 0
max = 0


for i in range(4):
    n, m = map(int, sys.stdin.readline().split())
    value -= n
    value += m

    if value > max:
        max = value
    

print(max)