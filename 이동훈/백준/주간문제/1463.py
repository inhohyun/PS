# 백준 1463 1로 만들기
import sys
input = sys.stdin.readline


n = int(input())

count = [0] * (n+1)

# while n != 1:
      
#       if (n-1) % 3 == 0:
#           n -= 1
#           count += 1

#       elif n % 3 == 0:
#         # print("3으로 나눠짐")
#         n /= 3
#         count += 1
#         # print(n)

#       elif n % 2 == 0: 
#           # print("2로 나눠짐")
#           count += 1
#           n /= 2
#           # print(n)

#       else:
#           n -= 1
#           count += 1



# print(count)



for i in range(2, n+1):
    count[i] = count[i-1] + 1

    if i % 2 == 0:
        count[i] = min(count[i], count[i//2]+1)
    if i % 3 == 0:
        count[i] = min(count[i], count[i//3] + 1)

print(count[n])