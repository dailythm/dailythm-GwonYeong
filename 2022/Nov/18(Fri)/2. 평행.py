# https://school.programmers.co.kr/learn/courses/30/lessons/120875

def solution(dots):
    arr = []
    for i in range(len(dots)-1):
        for j in range(i+1, len(dots)):
            if dots[i][0] - dots[j][0] != 0:
                
                ar = (dots[i][1] - dots[j][1])/ (dots[i][0] - dots[j][0])
            else:
                ar = 1
            print(i, j)
            if(ar in arr):
                return 1
            arr.append(ar)
            
    return 0