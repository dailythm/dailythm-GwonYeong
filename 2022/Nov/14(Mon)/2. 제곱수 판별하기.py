# https://school.programmers.co.kr/learn/courses/30/lessons/120909

def solution(n):
    i = 2
    while i * i <= n:
        if n == (i * i):
            return 1
        i += 1
    return 2
    