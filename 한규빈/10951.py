# 별도의 입력 갯수를 정하지 않고 계속 입력받기 위해 while문 사용
while True:
    # EOF를 통해서 프로그램이 종료되는 구조임.
    try:
        a,b=map(int,input().split())
        print(a+b)
    # EOF가 발생한 경우, EOFError라는 예외가 발생하여, 이 예외를 처리
    except EOFError:
        # 상위에서 동작하는 반복문을 중지하고, 반복문을 빠져 나옴.
        break