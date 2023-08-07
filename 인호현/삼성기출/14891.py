# 왜 못풀었는지 파악하기 -> 로직 파악하고 나만의 코드로 다시 구현
# deque를 이용해서 배열 돌리기
import collections
# 톱니바퀴 배열
s= []
for _ in range(4):
    s.append(collections.deque(list(input())))

K = int(input())
R = [list(map(int, input().split())) for _ in range(K)]

# 왼쪽 톱니바퀴 확인
def left(num, direction):
    # 첫번째 톱니바퀴는 확인 안함
    if num < 0:
        return
    
    if s[num][2] != s[num+1][6]: #극이 다른 경우
        left(num-1, -direction) # 그 왼쪽 톱니바퀴도 조사
        s[num].rotate(direction) # 현재 톱니바퀴는 회전

def right(num, direction):
    if num > 3:
        return 
    if s[num][6] != s[num-1][2]: # 극이 다른 경우
        right(num+1, -direction)
        s[num].rotate(direction)

for i in range(K):
    num = R[i][0] -1 # 돌아가는 톱니바퀴
    direction = R[i][1] # 시계, 반시계 방향
    left(num-1, -direction) # 왼쪽 조사
    right(num+1, -direction) # 오른쪽 조사
    s[num].rotate(direction)

res = 0
if s[0][0] == '1':
    res += 1
if s[1][0] == '1':
    res += 2
if s[2][0] == '1':
    res += 4
if s[3][0] == '1':
    res += 8

print(res)
