# 백준 1427 소트인사이드 실버5

n = input()

arr = []

num = len(n)

# value = n.sort


for i in range(num):
    arr.append(int(n[i]))
    # print(arr[i])

arr.sort(reverse=True)

for i in arr:
    print(i, end='')

# print(arrs)