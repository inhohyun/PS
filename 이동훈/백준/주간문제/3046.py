# 백준 3046 R2



# r1의 값, 평균 값
n,m = map(int, input().split())



r2 = 0



# m = (n + r2) / 2

# 3 = 4 + r2 / 2

# 3 * 2 = 4 + r2

# 6 = 4 + r2

# 6 - 4 = r2

r2 = m * 2 - n

print(r2)