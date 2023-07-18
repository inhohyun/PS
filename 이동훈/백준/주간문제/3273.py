import sys

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

x = int(sys.stdin.readline())


count = 0
arr.sort()


# 투포인터
start = 0

end = n-1





while start < end:
    
    value = arr[start] + arr[end]
    
    if value == x:
        count += 1
        start += 1

    elif value < x:
        start += 1
        

    else:
        end -= 1

print(count)

