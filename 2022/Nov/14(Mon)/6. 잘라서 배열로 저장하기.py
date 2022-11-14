# https://school.programmers.co.kr/learn/courses/30/lessons/120913#

def solution(my_str, n):
    answer = []
    
    i = 0
    k = 1
    while 1 :
        if i >= len(my_str):
            
            break
        answer.append(my_str[i:n * k])
        i += n
        k += 1
    return answer