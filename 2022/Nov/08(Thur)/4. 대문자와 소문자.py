# https://school.programmers.co.kr/learn/challenges/beginner?order=acceptance_desc

def solution(my_string):
    answer = ''
    for i in my_string:
        if i.isupper():
            answer += i.lower()
        else :
            answer += i.upper()
    return answer