# https://school.programmers.co.kr/learn/courses/30/lessons/132267

def solution(a, b, n):
    answer = 0
    count = n
    while count >= a:
        
        answer += (count // a) * b
        count = (count // a) * b + (count % a)
    return answer