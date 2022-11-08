# https://school.programmers.co.kr/learn/courses/30/lessons/120890?language=python3

import math
def solution(array, n):
    arr = []
    for i in array:
        arr.append(math.fabs(i - n))
    min_ = arr[0]
    answer = array[0]
    for l in range(len(array)):
        if min_ > arr[l] :
            min_ = arr[l]
            answer = array[l]
        elif min_ == arr[l]:
            answer = min(answer, array[l])
    # for i in array:
        
    return answer