n,m = map(int, input().split())

lab = []
for i in range(n):
    lab.append(list(map(int, input().split())))

# 입력값이 적음 -> 전부다 완탐으로 진행 가능
# dfs로 임의로 1을 3개 바꿔가며 지정하고 2근처를 모두 2로 바꿈
# 0의 개수가 제일 많은것을 출력
