# https://school.programmers.co.kr/learn/courses/30/lessons/120818?language=python3

def solution(price):
    discount = 0
    if price >= 100000:
        discount = 5
    if price >= 300000:
        discount = 10
    if price >= 500000:
        discount = 20
    
    return int(price * ((100 - discount) / 100))