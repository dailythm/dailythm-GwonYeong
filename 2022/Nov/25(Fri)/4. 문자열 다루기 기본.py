# https://school.programmers.co.kr/learn/courses/30/lessons/12918?language=python3

def solution(s):
    answer = True
    if len(s) == 4 or len(s) == 6:
        pass
    else:
        return False
    try:
        s = int(s)
    except:
        return False
    
   
    return answer