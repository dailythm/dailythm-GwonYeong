# https://school.programmers.co.kr/learn/courses/30/lessons/120845?language=python3

def solution(box, n):
    answer = 0
    r1 = box[0] // n
    r2 = box[1] // n
    r3 = box[2] // n
    
    return r1 * r2 * r3