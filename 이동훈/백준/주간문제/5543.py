# 백준 5543 상근날드
# 햄버거와 음료의 가격이 주어졌을 때, 가장 싼 세트 메뉴의 가격을 출력하는 프로그램을 작성해라

# 입력 값은 5개
# 첫째 줄에는 상덕버거, 둘째 줄에는 중덕버거, 
# 셋째 줄에는 하덕버거의 가격이 주어진다. 넷째 줄에는 콜라의 가격, 다섯째 줄에는 사이다의 가격이 주어진다
# 자신이 원하는 햄버거와 음료를 하나씩 골라, 세트로 구매하면, 가격의 합계에서 50원을 뺀 가격이 세트 메뉴의 가격

sum = 0
arr = []
arr2 = []
min = 99999
min2 = 99999

for i in range(3):
    n = int(input())
    arr.append(n)

for i in range(2):
    n = int(input())
    arr.append(n)

# print(arr)

for i in range(3):
    if min > int(arr[i]):
        min = int(arr[i])

for i in range(2):
    if min2 > int(arr[i+3]):
        min2 = int(arr[i+3])

mins = min + min2 - 50

print(mins)


