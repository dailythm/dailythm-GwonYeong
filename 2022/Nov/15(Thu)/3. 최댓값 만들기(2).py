# https://school.programmers.co.kr/learn/courses/30/lessons/120862

def solution(numbers):
    answer = 0
    max_num = numbers[0] * numbers[1]
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if max_num < numbers[i] * numbers[j] and i != j:
                max_num = numbers[i] * numbers[j]
    return max_num