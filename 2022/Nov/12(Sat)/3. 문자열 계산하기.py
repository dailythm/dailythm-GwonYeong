# https://school.programmers.co.kr/learn/courses/30/lessons/120902

# 생각보다 어려웠음 ;

def solution(my_string):
    arr = my_string.split(' ')
    result = int(arr[0])
    for i in range(1, len(arr), 2):
        if arr[i] == '+':
            result += int(arr[i+1])
        else:
            result -= int(arr[i+1])
        
        
    return result