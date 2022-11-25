# https://school.programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    answer = True
    P = 0
    Y = 0
    for i in s:
        if i == 'p' or i == 'P':
            P += 1
        elif i == 'y' or i == 'Y':
            Y += 1
    if P != Y:
        answer = False
    

    return answer