from sys import stdin

# 파이썬 내 반올림 함수(round)의 '오사오입' 방식이 아닌 일반 '사사오입' 방식의 결과를 도출하기 위해 별도의 함수 정의
# 공식 : round(<대상 값>+10^(-<대상 값의 길이>-1))
#  => 예시 : (대상=3.5) => 3.5+10^(-3-1) = 3.5+10^-4 = 3.5+0.0001 = 3.5001
def round_func(value):
    return round(value+10**(-len(str(value))-1))

n=int(stdin.readline().rstrip())
res=0

# 데이터의 갯수가 0(없음)일 수도 있으므로 0인지 검증
if n>0:
    arr=[]
    sum=0
    for _ in range(n):
        a=int(stdin.readline().rstrip())
        arr.append(a)
        sum+=a
    arr.sort()

    # 제외해야하는 범위 산출 - 반올림 필요
    b=round_func(n*0.15)
    # 제외된 범위의 합계를 저장할 변수
    bsum=0
    for i in range(b):
        # 리스트는 정렬 상태이므로, 앞쪽에는 최소, 뒤쪽에는 최대 값이 들어있게 됨.
        # 제외 범위 앞쪽과 뒤쪽의 값을 더하여 합계 변수에 더함.
        bsum+=(arr[i]+arr[-i-1])

    # 결과 값 계산(총합에서 범위 외 합계 제외, 개수 또한 제외) - 반올림 필요
    res=round_func((sum-bsum)/(n-b*2))

print(res)