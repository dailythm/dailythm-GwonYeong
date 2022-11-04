# https://school.programmers.co.kr/learn/courses/30/lessons/120839

def solution(rsp):
    answer = ''
    for i in rsp:
        
        if i == "0":
            answer += "5"
            continue
        elif i == "2":
            answer += "0"
            continue
        else :
            answer += "2"
    return answer