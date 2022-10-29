# https://school.programmers.co.kr/learn/courses/30/lessons/120814

def recursive(pizza,n):
    if n / pizza <= 7:
        return pizza
    return recursive(pizza+1,n)

def solution(n):
    return recursive(1,n)
        
   