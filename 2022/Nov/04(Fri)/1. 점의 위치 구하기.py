# https://school.programmers.co.kr/learn/courses/30/lessons/120841

def solution(dot):
    if dot[0] < 0:
        if dot[1] < 0:
            return 3
        else:
            return 2
    else:
        if dot[1] < 0:
            return 4
        else:
            return 1
            
    