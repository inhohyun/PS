# 백준 1085 직시각형에서 탈출 브론즈3

x, y, w, h = map(int, input().split())

print(min(x, y, w-x, h-y))