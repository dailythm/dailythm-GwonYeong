# https://school.programmers.co.kr/learn/courses/30/lessons/120846

arr = []
arr.index
def solution(n):
    answer = 0
    for i in range(1, n+1):
        for j in range(2,i):
            if i != j and i % j == 0:
                answer += 1
                break
    
    return answer
    