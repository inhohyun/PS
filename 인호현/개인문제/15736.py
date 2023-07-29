# 초기의 깃발은 모두 청색?
# 1. 일단 완전탐색으로 구현해보기 -> 시간초과 날것임
n = int(input())
# 이 문제는 제곱근을 구하는 문제였음
answer = int(n **0.5)
print(answer)

# # 0은 청, 백은 1
# flag = [0] * (n+1)
# flag [0] = 10
# for i in range(1, n+1):
#     for j in range(i, n, i):
#         if flag[j] == 0:
#             flag[j] = 1
#         elif flag[j] == 1:
#             flag[j] = 0

# print(flag.count(1))  

