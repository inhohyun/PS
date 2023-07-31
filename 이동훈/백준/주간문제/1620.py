# 백준 1620

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

value = {}


# 숫자와 입력한 텍스트 값이 각각 딕셔너리 형태에서 key와 value 값을 넣을 수 있게 구현

for i in range(1, n+1):
    x = input().rstrip()
    value[i] = x
    value[x] = i

# x는 찾고자 하는 값을 입력한다, 숫자가 입력시 그 숫자에 위치한 텍스트 값을 반대인 경우도 마찬가지로 적어주면 된다

for j in range(m):
    x = input().rstrip()
    # 숫자인지 문자형인지 판별하는 메서드를 이용해 문제를 해결
    if x.isdigit():
        print(value[int(x)])
    
    else:
        print(value[x])
        
# print(value)