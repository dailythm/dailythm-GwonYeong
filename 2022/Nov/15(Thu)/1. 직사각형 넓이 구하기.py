# https://school.programmers.co.kr/learn/courses/30/lessons/120860

import math

def solution(dots):
   
    for i in range(1,len(dots)):
        if dots[0][0] == dots[i][0]:
            y =  math.fabs(dots[0][1]- dots[i][1])
        if dots[0][1] == dots[i][1]:
            x = math.fabs(dots[0][0] - dots[i][0])
    return x * y