arr=[]
for i in range(9):
    arr.append([int(input()),i+1])

arr.sort()
print(arr[-1][0])
print(arr[-1][1])