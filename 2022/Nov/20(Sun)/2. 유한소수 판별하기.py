# https://school.programmers.co.kr/learn/courses/30/lessons/120878

import math 

def solution(a, b):
    answer = 0
    gcd = math.gcd(a,b)
    
    b = b // gcd
    while 1:
        if b == 1:
            return 1
        if b % 2 == 0:
            b /= 2
            continue
        elif b % 5 == 0:
            b /= 5
            continue
        return 2
    