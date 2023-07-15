import sys

# n은 동전의 개수, k는 총 금액
n, k = map(int, map(int, sys.stdin.readline().split()))

arr = []
count = 0

# 빈 배열에 동전 가치를 추가
for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

# 오름차순 정렬
arr.sort(reverse=True)
print(arr)


for i in arr:
    if k != 0:
      count += int(k // i)
      k %= i

print(count)