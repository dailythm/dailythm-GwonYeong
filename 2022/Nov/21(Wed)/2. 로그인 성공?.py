# https://school.programmers.co.kr/learn/courses/30/lessons/120883

def solution(id_pw, db):
    answer = ''
    idx = 0
    for user in db:
        if id_pw == user:
            return 'login'
        if id_pw[0] == user[0]:
            return "wrong pw"
    
    return "fail"
        
    