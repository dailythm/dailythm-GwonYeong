# https://school.programmers.co.kr/learn/courses/30/lessons/120886

def solution(before, after):
    answer = ''
    
    for i in before:
        if i not in after:
            return 0
        after =after.replace(i, '',1)
    return 1
