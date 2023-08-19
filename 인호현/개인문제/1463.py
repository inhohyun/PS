# 역순으로 1을 x로 만들기
x= int(input())
cnt = 0
tmp = 1
# 3을 최대한 곱하기
while x > tmp:
    tmp *= 3
    cnt += 1

if (x - tmp) % 2 == 0:
    cnt += (x - tmp) // 2
else:
    cnt += x - tmp 

print(cnt)


