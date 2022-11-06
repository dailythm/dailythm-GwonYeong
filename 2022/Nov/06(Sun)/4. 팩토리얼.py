# https://school.programmers.co.kr/learn/courses/30/lessons/120848

def factorial(num):
    if num == 1:
        return num
    return num * factorial(num-1)

def solution(n):
    i = 1
    while 1 :
        if factorial(i) > n:
            return i - 1
        i +=1
    