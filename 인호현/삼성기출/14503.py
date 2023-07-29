# 0 : 위, 1 : 오른쪽, 2 : 아래, 3 : 왼쪽
# 0 : 청소되지 않음, 1 : 벽

n, m = map(int, input().split())
r, c, d = map(int, input().split())

room = []
for i in range(n):
    room.append(list(map(int, input().split())))


while True:
    # 현재 위치 청소
    room[r][c] = 1
    

# 지나간 자리를 전부 1로 만들면서 진행
