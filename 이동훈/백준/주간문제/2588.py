# 백준 2588 곱셈 브론즈 3

import sys

n = int(sys.stdin.readline())

m = sys.stdin.readline()



value = 0
lens = len(m)

for i in range(lens-2, -1, -1):
    # print(m[i])

    
    value = int(m[i]) * n
    print(value)

value = n * int(m)
print(value)