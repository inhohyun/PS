# 1978 소수 찾기 브론즈 2

n = int(input())


m = list(map(int,input().split()))
count = 0

for x in m:
    for i in range(2, x+1):
      if x % i == 0:
        if x == i:
          count += 1

        break
    
print(count)
