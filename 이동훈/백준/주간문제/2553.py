# 백준 2553 마지막 팩토리얼 수

import sys
input = sys.stdin.readline

n = int(input())
value = 1

for i in range(1, n+1):
    value = value * i

ch = str(value)
# print(ch[-1])
# print(ch[-2])
# def factor(num):
#   if str(num[-1]) != "0":
#       print(num[-1])

#   else:
#       factor(num[:-1])
      

# factor(ch)

for j in reversed(ch):
    if j != "0":
        print(j)
        break