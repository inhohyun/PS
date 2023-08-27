n, m = map(int, input().split())

numbers = sorted(list(map(int, input().split())))
ans = []
visited = [False] * n
def dfs():
    
    if len(ans) == m:
        print(*ans)
        return
    remember = 0
    for i in range( n):
        # remember를 활용하여 같은 수열이 반복되는 것을 방지한다.(배열의 같은 숫자가 반복되는 것과는 다른 것이다.)
        if remember != numbers[i]:
            if not visited[i]:

                ans.append(numbers[i])
                visited[i] = True
                remember = numbers[i]
                
            
                dfs()

                ans.pop()
                visited[i] = False
dfs()