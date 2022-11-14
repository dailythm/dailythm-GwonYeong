# https://school.programmers.co.kr/learn/courses/30/lessons/120585

def solution(array, height):
    answer = 0
    array.sort(reverse = True)
    for i in range(len(array)):
        if array[i] <= height:
            return i
    return len(array)