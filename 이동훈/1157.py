m = input().upper()
lists = list(set(m))

arr = []

for i in lists:
    cnt = m.count(i)
    arr.append(cnt)

if arr.count(max(arr)) > 1:
    print("?")

else:
    max_index = arr.index(max(arr))
    print(lists[max_index])
