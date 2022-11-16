# https://school.programmers.co.kr/learn/courses/30/lessons/120864?language=python3

def solution(my_string):
    answer = 0
    arr = ''
    for i in my_string:
        
        if not i.isalpha():
            arr += i
        else:
            arr += ' '
    arr = arr.split(' ')
    for i in arr:
        
        try:
            answer += int(i)
        except:
            continue
        
    
    return answer