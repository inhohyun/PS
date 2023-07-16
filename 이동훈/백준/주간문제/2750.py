# 백준 2750 수 정렬하기 브론즈2

n = int(input())

arr = []

# 숫자 값들을 리스트에 입력
for i in range(n):
    arr.append(int(input()))

# 리스트 정렬
arr.sort()

for i in range(len(arr)):
    print(arr[i])