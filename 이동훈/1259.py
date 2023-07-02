#1259번 문제 팰린드롬수


import sys

# 문자열 입력받기
data = input()  


while data != '0':
    # 문자열을 리스트로 변환
    arr = list(data)  
    
    # 리스트 뒤집기
    arr.reverse()  

    # 리스트를 문자열로 변환하여 비교
    if data == ''.join(arr):  
        print("yes")

    else:
        print("no")
    data = input()
    

