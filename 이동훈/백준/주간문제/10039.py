# 백준 10039 평균 점수

value = 0

for i in range(5):
    n = int(input())
    if n >= 40:
      value += n

    else:
      value += 40

print(value//5)