# https://school.programmers.co.kr/learn/courses/30/lessons/120847

def solution(numbers):
    answer = 0
    max_idx = numbers.index(max(numbers))
    max1 = numbers[max_idx]
    numbers[max_idx] = -1
    max2 = max(numbers)
    return max1 * max2