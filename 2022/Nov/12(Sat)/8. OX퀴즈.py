# https://school.programmers.co.kr/learn/courses/30/lessons/120907

def solution(quiz):
    answer = []
    for i in quiz:
        calc = i.split(' ')
        if(calc[1] == "+"):
            if int(calc[0]) + int(calc[2]) == int(calc[4]):
                answer.append('O')
            else:
                answer.append('X')
        else:
            if int(calc[0]) - int(calc[2]) == int(calc[4]):
                answer.append('O')
            else:
                answer.append('X')
    return answer