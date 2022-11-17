# https://school.programmers.co.kr/learn/courses/30/lessons/120868

def solution(sides):
    answer = 0
    low = min(sides)
    long = max(sides)
    m = long - low
    m = long - m
    
    n = low + long
    n = n - long - 1
    
    print(m,n)    
    return m + n