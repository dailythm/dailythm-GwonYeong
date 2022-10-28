# https://school.programmers.co.kr/learn/courses/30/lessons/120812

def solution(array):
    max_num = 0
    answer = 0
    for i in range(max(array)+1):
        freq = array.count(i)
        if max_num < freq:
            max_num = freq
            answer = i
        elif max_num == freq:
            answer = -1
                
         
    return answer