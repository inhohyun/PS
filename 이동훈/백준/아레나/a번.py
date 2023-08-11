import sys
input = sys.stdin.readline

arr = []
new_arr = {}
min = 99999
value = 0
for i in range(5):
    n = int(input())
    arr.append(n)
    


for i in arr:
    try:
        new_arr[i] += 1
    except:
        new_arr[i] = 1


for i in arr:
  if new_arr[i] == 3:
          # min = new_arr[i]
          value = i
          break

  elif min > new_arr[i]:
          
          min = new_arr[i]
          # print(min, new_arr[i], i)
          value = i
# print(new_arr)

# print(min)
print(value)