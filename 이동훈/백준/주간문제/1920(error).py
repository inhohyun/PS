# 백준 1920 수 찾기
# 시간 초과

import sys
input = sys.stdin.readline



n = int(input())
n_arr = list(map(int, input().split()))

m = int(input())
m_arr = list(map(int, input().split()))

arr = m_arr
count = 0

# print(n_arr, m_arr)


# for i in n_arr:
#     for j in m_arr:
#         if i == j:
#             # count+=1
#             print(m_arr[j])

for i in range(n):
    for j in range(m):
        if n_arr[i] == m_arr[j]:
            # print(m_arr[j])
            m_arr[j] = 1
        
for i in range(m):
    if m_arr[i] == 1:
        print(1)

    else:
        print(0)        

# print(m_arr)        
# print(count)
