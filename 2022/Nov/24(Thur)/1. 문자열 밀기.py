# https://school.programmers.co.kr/learn/courses/30/lessons/120921

def solution(A, B):
    answer = 0
    A = list(A)
    B = list(B)
    while 1:
        if answer > len(A):
            return -1
        if A == B:
            return answer
        A.insert(0 , A[-1])
        A.pop()
        answer+=1
        
    return answer