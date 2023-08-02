# 코딩테스트 책 

n, m, k = map(int, input().split())

z = list(map(int, input().split()))

count = 0
sum = 0

z.sort(reverse=True)

for i in range(m):
    if count // 3 != 0:
        sum += z[0]
        count += 1

    else:
        count += 1
        sum += z[1]

print(sum)