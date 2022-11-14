# https://school.programmers.co.kr/learn/courses/30/lessons/120911

def solution(my_string):
    
    my_string = my_string.lower()
    my_string = list(my_string)
    my_string.sort()
    result = ''.join(my_string)
    return result