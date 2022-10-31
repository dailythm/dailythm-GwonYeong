# https://school.programmers.co.kr/learn/courses/30/lessons/120822?language=python3

def solution(my_string):
    answer = ""
    for i in range(1, len(my_string)+1):
        answer += my_string[-i]
    
    
    return answer