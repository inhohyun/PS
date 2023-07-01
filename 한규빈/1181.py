# 데이터 개수(n)을 입력받음.
n=int(input())
# 데이터를 입력받아 쌓아둘 배열(리스트) 선언 및 초기화
iarr=[]

# 데이터 개수만큼 반복하여 데이터 받음.
for i in range(n):
  iarr.append(input())

# 새 배열 변수 선언 및 초기화 - set형을 사용하여 기존 입력받은 배열 변환 : 중복 값 제거
arr=list(set(iarr))
# print(type(arr))
# print(arr)

# 배열 요소를 알파벳 순서대로 정렬
arr.sort()
# print(arr)

# 정렬된 배열 요소를 다시 길이 순서대로 정렬
arr.sort(key=len)
# print(arr)

# 출력 - 실제 정렬된 배열 요소 개수만큼 반복하여 출력
for i in range(len(arr)):
  print(arr[i])
