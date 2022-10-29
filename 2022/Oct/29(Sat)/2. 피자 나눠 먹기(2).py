# https://school.programmers.co.kr/learn/courses/30/lessons/120815

def recursive(pizza, n):
    if pizza * 6 % n == 0:
        return pizza
    return recursive(pizza+1, n)

def solution(n):
    return recursive(1,n)