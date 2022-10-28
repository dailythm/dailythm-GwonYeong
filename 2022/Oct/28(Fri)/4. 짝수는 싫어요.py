# https://school.programmers.co.kr/learn/courses/30/lessons/120813

def solution(n):
    answer = []
    for i in range(n+1):
        if i % 2 == 1:
            answer.append(i)
    return answer