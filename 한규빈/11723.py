import sys
n=int(sys.stdin.readline().rstrip())
arr=set()

for _ in range(n):
    com=sys.stdin.readline().rstrip().split()

    if len(com)==1:
        if com[0]=="all":
            arr=set([i for i in range(1,21)])
        else:
            arr.clear()
    else:
        num=int(com[1])
        if com[0]=="add":
            arr.add(num)
        elif com[0]=="remove":
            arr.discard(num)
        elif com[0]=="check":
            if num in arr:
                print(1)
            else:
                print(0)
        elif com[0]=="toggle":
            if num in arr:
                arr.discard(num)
            else:
                arr.add(num)
