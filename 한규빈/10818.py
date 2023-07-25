from sys import stdin
n=int(stdin.readline().rstrip())
arr=list(map(int,stdin.readline().rstrip().split()))

# 정렬을 한번 하고나서 맨 처음과 끝을 출력하여 최대, 최소값을 출력
arr.sort()
print(arr[0],arr[-1])