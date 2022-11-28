# https://school.programmers.co.kr/learn/courses/30/lessons/131128

def solution(X, Y):
    answer = []
    for i in range(9,-1,-1):
        x = X.count(str(i))
        y = Y.count(str(i))
        for j in range(min(x,y)):
            answer.append(str(i))
    answer = ''.join(answer)
    if answer == '':
        return '-1'
    if answer[0] == '0':
        return '0'
    return answer