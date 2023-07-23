# 백준 2576 홀수

sum = 0
min = 99999
for i in range(7):
    n = int(input())
    if n % 2 == 1:
        sum += n
        if min > n:
            min = n

if sum >= 1:
  print(sum)
  print(min)

else:
    print(-1)