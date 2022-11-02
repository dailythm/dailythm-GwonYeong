# https://school.programmers.co.kr/learn/courses/30/lessons/120835

def solution(emergency):
    answer = [0] * len(emergency)
    rank = 1
    for i in range(len(emergency)):
        idx = emergency.index(max(emergency))
        answer[idx] = rank
        rank += 1
        emergency[idx] = 0
    return answer