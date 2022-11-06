# https://school.programmers.co.kr/learn/courses/30/lessons/120840

def factorial(num):
    
    if num == 1:
        return num
    return num * factorial(num-1)

def solution(balls, share):
    answer = 0
    if(balls == share):
        return 1
    answer = factorial(balls)/ (factorial(balls - share) * factorial(share))
    return answer