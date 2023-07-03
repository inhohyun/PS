# 1436번 영화감독 숌
import sys

n = int(sys.stdin.readline())

num = 665
cnt = 0
arr = []

# num을 증가시키면서 666이 연결된 부분 찾기 
while True:
    num+=1

    # 666이 연결된 부분 빈 배열에 가져오기
    if(str(num).count("666") >= 1):
      arr.append(num)

      
      if(len(arr) == n):
          break;

print(arr[-1])