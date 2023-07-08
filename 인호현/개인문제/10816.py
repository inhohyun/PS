from sys import stdin
from collections import Counter
_ = stdin.readline()
N = stdin.readline().split()
_ = stdin.readline()
M = stdin.readline().split()

C = Counter(N)
# 아래 코드 설명
print(' '.join(f'{C[m]}' if m in C else '0' for m in M))
