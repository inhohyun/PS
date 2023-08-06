# 끝말잇기

# import sys
# input = sys.stdin.readline

n = int(input())

arr = []
arr_2 = []

value = 0

cnt1 = 0
cnt2 = 0

x = 0

for i in range(n):
    s = input().strip()
    arr.append(s)
    if s == '?':
        value = i

cnt1 = arr[value-1][-1]
cnt2 = arr[value+1][0]

# print(arr)
# print(value, cnt1, cnt2)

new_arr = []

m = int(input())


for j in range(m):
    v = input().strip()
    new_arr.append(v)
    # print(v[0])
    # print(v[-1])
    if v[0] == cnt1 and v[-1] == cnt2:
          for k in arr:
              print(k, v)
              if k == v:
                  
                  break
              # else:
    x = v
                  

print(x)
