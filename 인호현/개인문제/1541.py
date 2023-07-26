# 1. 주어진 문자열을 -를 기준으로 나눈다.
# 2. 나눠진 문자열을 다시 +를 기준으로 나눈다?


arr = list(input().split('-'))
ans = []
for i in range(len(arr)):
    arr[i] = arr[i].split('+')
    ans.append(sum(map(int, arr[i])))

answer = ans[0]

for i in range(1, len(ans)):
    answer -= ans[i]

print(answer)
