n = int(input())


for _ in range(n):
    m, x = input().split()
    for i in x:
        print(i*int(m), end='')
    print()
