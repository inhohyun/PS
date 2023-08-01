n = int(input())
result = 1
arr = []
count = 0
cnt = 0

def factoreal(num):

    global result
    global count

    while True:
       if num > 0:
          result = result * num
          num -= 1
        #   print(result)
          if str(result)[-1] == "0":
             count += 1


       elif num == 0:
          break

    return result

    # for i in range(num):
    #   arr.append(i)
    # print(arr)

k = -1
ts = len(str(result))

while True:
   if result // 10 == 0 :
      cnt += 1
      result //= 10
      print(result)
   else :
      break



factoreal(n)
print(result, count-1)
print(cnt)
