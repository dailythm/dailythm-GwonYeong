# https://school.programmers.co.kr/learn/courses/30/lessons/120837?language=python3

def solution(hp):
    answer = 0
    while hp > 0:
        if hp >= 5:
            answer +=1
            hp -= 5
            continue
        elif hp >= 3:
            answer +=1
            hp -= 3
            continue
        else :
            answer +=1
            hp -= 1
    
    return answer