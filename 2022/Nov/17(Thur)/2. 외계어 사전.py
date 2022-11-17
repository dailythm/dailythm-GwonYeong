# https://school.programmers.co.kr/learn/courses/30/lessons/120869

def solution(spell, dic):
    answer = 0
    for i in dic:
        for j in range(len(spell)):
            if i.count(spell[j]) == 1:
                if j == len(spell) -1:
                    return 1
            else:
                break
    return 2