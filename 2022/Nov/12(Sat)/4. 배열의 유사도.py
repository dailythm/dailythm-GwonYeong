# https://school.programmers.co.kr/learn/courses/30/lessons/120903

def solution(s1, s2):
    answer = 0
    for i in s1:
        for j in s2:
            if i == j:
                answer +=1
                break
    return answer