# 백준 1940 주몽 실버4

n = int(input())
m = int(input())

x = list(map(int, input().split()))

start = 0
end = n-1

count = 0
# print(n, m, x)

# for i in x:
#     print(i)

x.sort()

print(x)

while start < end:
    if x[start] + x[end] == m:
        count += 1
        print("이건 합이 일치 하는 경우 : ", x[start] , x[end])
        start += 1
        end -= 1
        print("그 후 : ", x[start] , x[end])

    elif x[start] + x[end] < m:
            start += 1

    else:
         end -= 1
         
         
           

print(count)