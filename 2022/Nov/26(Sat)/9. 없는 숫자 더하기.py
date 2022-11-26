# https://school.programmers.co.kr/learn/courses/30/lessons/86051

def solution(numbers):
    answer = 45
    for i in numbers:
        answer -= i
    return answer
    