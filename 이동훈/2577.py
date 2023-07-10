n = int(input())
m = int(input())
x = int(input())

result = str(n * m * x)

lr = len(result)

for i in range(10):
    
    rn = result.count(str(i))
    print(rn)

