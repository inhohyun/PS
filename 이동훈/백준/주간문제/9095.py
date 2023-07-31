# 백준 9095 1,2,3 더하기 실버3 - 발표 문제

# 테스트 케이스 입력
n = int(input())


# 1,2,3의 합의 계산의 횟수를 출력

def count(num):
    
    # 매개변수가 1,2,3 일때 경우의 수를 지정
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    
    # 매개변수가 4, 5 두가지 경우를 가정한다 했을 때 4의 경우는 7개, 5의 경우는 13의 계산 횟수가 생긴다
    # 이때 4는 첫번째, 두번째, 세번쨰 경우의 수를 합친 횟수와 같고 5 역시 2,3,4 의 경우의 횟수를 더한 값과 같다
    # 이를 이용해 dp 문제이기에 위의 점화식을 통해서 값을 출력한다
    else :
        return count(num-1) + count(num-2) + count(num-3) 
    

for i in range(n):
    num = int(input())
    print(count(num))

