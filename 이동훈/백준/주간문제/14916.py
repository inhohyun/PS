# 백준 14916 거스름돈 실버5

n = int(input())

count = 0


while n > 1:
    # 5를 나눈 나머지가 떨어진다면 구한다
    if n % 5 == 0:
        count += n//5
        n %= 5
        # print("5의 ",n, count)                
    
    

    # 5를 나눌수 있을 때까지 n을 2를 줄인다
    elif n >= 2 and n != 3:
        count += 1
        n -= 2
        # print("2의 ", n, count)
    
    else : 
        # print(-1)
        break

if count >= 1:
    print(count)
else:
    print(-1)

