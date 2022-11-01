# https://school.programmers.co.kr/learn/courses/30/lessons/120829

def solution(angle):
    angle /= 90
    if angle < 1:
        return 1
    elif angle == 1:
        return 2
    elif angle == 2:
        return 4
    else: 
        return 3
    