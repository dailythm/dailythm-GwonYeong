# https://school.programmers.co.kr/learn/courses/30/lessons/120816

def recursive(slice, pizza, n ):
    if slice * pizza >= n:
        return pizza
    return recursive(slice, pizza + 1, n)

def solution(slice, n):
    return recursive(slice, 1, n)