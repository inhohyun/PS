n = int(input())
# 다음에 다시 풀어보기
hint = [list(map(int, input().split())) for _ in range(4)]

answer = 0
for a in range(1, 10):
    for b in range(10):
        for c in range(10):
            
            # 자릿수가 겹칠 경우 숫자야구 불가
            if(a == b or b==c or c== a):
                continue

            cnt = 0
            # 하나의 수가 정해졌다면 
            for arr in hint:
                number = arr[0]
                ball = arr[1]
                strike = arr[2]

                ball_count = 0
                strike_count = 0
            # a,b,c라는 숫자를
            # number하고 비교
            # 자릿수를 나누어 strike와 ball을 구분하기
                num = str(a *100 +b*10 + c)
                check_a = int(str(number)[0])
                check_b = int(str(number)[1])
                check_c = int(str(number)[2])
                # ball인 경우 -> 자릿수는 다른데 있긴 있음
                if str(check_a) in num and check_a != a:
                    ball_count += 1
                if str(check_b) in num and check_b != b:
                    ball_count += 1
                if str(check_c) in num and check_c != c:
                    ball_count += 1
                # strike인 경우 -> 자릿수와 일치
                if check_a == a:
                    strike_count += 1
                if check_b == b:
                    strike_count += 1
                if check_c == c:
                    strike_count += 1
                    

                # 힌트를 통과한 개수
                if ball == ball_count and strike == strike_count:
                    cnt += 1
                    
            if cnt == n:
                answer += 1

print(answer)