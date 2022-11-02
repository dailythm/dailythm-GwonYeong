# https://school.programmers.co.kr/learn/courses/30/lessons/120834
def solution(age):
    answer = ""
    for i in str(age):
        answer += chr(97+int(i))
    return answer