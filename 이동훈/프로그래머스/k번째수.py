# k 번째의 수

# i, j, k = map(int, input().split())

arrs = []

def sorteds(arr, commands):

  list_len = len(commands)
  
  for x in range(list_len):

    i = commands[x][0]
    j = commands[x][1]
    k = commands[x][2]

    value_arr = arr[i-1:j]

    sorted_arr = sorted(value_arr)
    # print(sorted_arr[k-1])
    arrs.append(sorted_arr[k-1])
    
  print(arrs)

arr1 = [1,5,2,6,3,7,4]
commands1 = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

sorteds(arr1, commands1)