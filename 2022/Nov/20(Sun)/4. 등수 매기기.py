# https://school.programmers.co.kr/learn/courses/30/lessons/120882

def solution(score):
    dict={}
    q=[]
    for i in score:
        q.append(sum(i)/2)

    for index, avg in enumerate(sorted(q,reverse=True), start=1):
        if avg not in dict:
            dict[avg] = index

    return [dict[avg] for avg in q]