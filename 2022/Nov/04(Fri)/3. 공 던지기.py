# https://school.programmers.co.kr/learn/courses/30/lessons/120843

def solution(numbers, k):
    curr = 1
    while k > 1:
        curr += 2
        if curr > numbers[-1]:
            curr -= numbers[-1]
        k -= 1
    return curr