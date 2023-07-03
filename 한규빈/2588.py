a=int(input())
b1=b2=int(input())

for i in range(1,4):
    print(a*(b2%10))
    b2=int(b2/10)

print(a*b1)