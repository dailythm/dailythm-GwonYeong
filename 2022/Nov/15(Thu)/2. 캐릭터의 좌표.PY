# https://school.programmers.co.kr/learn/courses/30/lessons/120861

import math

def solution(keyinput, board):
    answer = [0,0]
    for i in keyinput:
        if i == 'up':
            if answer[1] + 1 <= board[1]//2 :
                answer[1] += 1
        elif i == 'down':
            if answer[1] -1>= -(board[1]//2) :
                answer[1] -= 1
        elif i == 'left':
            if answer[0]  - 1>= -(board[0]//2) :
                answer[0] -= 1
        elif i == 'right':
            if answer[0] + 1<=  board[0]//2 :
                answer[0] += 1
    return answer