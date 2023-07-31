#백준 1920 수 찾기
# 시간 초과

import sys
input = sys.stdin.readline

n = int(input())
n_arr = list(map(int, input().split()))

m = int(input())
m_arr = list(map(int, input().split()))

start = 0
end = n-1

n_arr.sort()

def check(start, end, n_arr, c):

        if start > end:
             return print(0)
        mid = (start + end) // 2
        if c == n_arr[mid]:
            return print(1)
        elif c < n_arr[mid]:
            return check(start, mid-1, n_arr, c)
        else:
            return check(mid+1, end, n_arr, c)

for c in m_arr:
    check(start, end, n_arr ,c)