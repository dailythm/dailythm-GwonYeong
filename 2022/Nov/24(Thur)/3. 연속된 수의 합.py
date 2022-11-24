# https://school.programmers.co.kr/learn/courses/30/lessons/120923

def solution(num, total):
    answer = []
    temp = 1000
    while 1:
        result = 0
        answer = []
        for i in range(num):
            result += temp -i
            answer.append(temp-i)
        if result == total:
            
            return sorted(answer)
        temp -= 1
        
 