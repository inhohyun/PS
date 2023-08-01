# 백준 2231 분해합

n = input()
arr = list(map(int, n))
value = int(n)

# for i in arr:
#     value += i    

# 생성자를 찾기 시작 -> 1부터 입력 값 즉 분해 값까지 모든 코드를 반복하여서 값을 찾는다
# i가 생성자를 나타낸다
for i in range(1, n+1):

    num = list(map(int, str(i) ))
    value = i + sum(num)

    if value == n:
        print(i)
        break

    else:
        print(0)


print(n)
print(arr)
print(value)

# 216 -> 198 + 1 + 9 + 8 => 18 + 198