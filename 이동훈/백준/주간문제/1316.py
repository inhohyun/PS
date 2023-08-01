# 백준 1316 그룹 단어 체크 실버5
# 다시 풀기

n = int(input())

count = n   


for i in range(n):
    m = input()
    # 알파벳 순서대로 비교
    for j in range(len(m)-1):

        # 알파벳이 인덱스가 연속적으로 동일하다면 통과
        if m[j] == m[j+1]:
            
            continue

        # 알파벳이 연속적이지 않는데 동일한 문자가 있다면 그룹단어 x
        elif m[j] in m[j+1:]:
            count-=1
            break

print(count)   