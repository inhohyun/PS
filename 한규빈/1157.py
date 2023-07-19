import sys
s=sys.stdin.readline().rstrip().upper()
cnt=dict()

for i in range(len(s)):
    if not s[i] in cnt:
        cnt[s[i]]=0
    cnt[s[i]]+=1
    # print(s[i],cnt[s[i]])

max=[0,'A',False]
for i in range(ord('A'),ord('a')):
    k=chr(i)
    if not k in cnt:
        continue
    else:
        # print(cnt[k])
        if max[0]<cnt[k]:
            max[0]=cnt[k]
            max[1]=k
            max[2]=False
        elif max[0]==cnt[k]:
            max[2]=True

if max[2]==True:
    print("?")
else:
    print(max[1])