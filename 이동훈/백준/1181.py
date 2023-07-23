n = int(input())
arr = []

for i in range(n):
  arr.append(input())

sets = set(arr)
arr = list(sets)
arr.sort()
arr.sort(key=len)

for i in arr:
  print(i)
