from sys import stdin
n=int(stdin.readline().rstrip())
pattern=""
plen=0

for _ in range(n):
    name=stdin.readline().rstrip()
    if plen==0:
        pattern=name
        plen=len(pattern)
    else:
        for i in range(plen):
            if pattern[i]=='?' or pattern[i]==name[i]:
                continue
            else:
                pattern=pattern[:i]+'?'+pattern[i+1:]

print(pattern)