# 백준 1003번 실버 3

# 0과 1의 호출 횟수를 저장할 리스트 생성
zero = [1, 0, 1] # 0일때 호출 1, 1일때 호출 0, 2일때는 1
one = [0, 1, 1] # 0일때 호출 0, 1일때 호출 1, 2일때는 1

# fib(n) = fib(n-1) + fib(n-2)
# 피보나치 n에서 0, 1 의 호출 횟수 = 피보나치 n-1 에서 0,1 의 호출횟수 + 피보나치 n-2 에서 0,1 의 호출횟수

def fibonacci(num):
    length = len(zero)
    if num >= length:
        for i in range(length, num+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print(zero[num], one[num])

T = int(input())

for _ in range(T):
    fibonacci(int(input()))