n = int(input())
m = str(input())

arr = []
result = 0
for i in range(len(m)):
    arr.append(int(m[i]))
    result += arr[i]

print(result)
