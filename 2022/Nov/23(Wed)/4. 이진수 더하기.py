# https://school.programmers.co.kr/learn/courses/30/lessons/120885

def solution(bin1, bin2):
    answer = 0
    answer +=int(bin1, 2) + int(bin2, 2)
    answer = bin(answer)
    answer = answer.replace('0b', '')
    return answer