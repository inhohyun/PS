# 백준 막대기 1094 실버5
# 기존 64cm의 막대를 입력값 n의 길이의 막대를 만든다

# 입력값
n = int(input())
stick = 64
arr = []
count = 0
value = 0


    

while (1):
    if (n < stick):
      stick = stick // 2
      
    
    else:
      n = n-stick
      count += 1
      if(n==0):
        break

print(count)



