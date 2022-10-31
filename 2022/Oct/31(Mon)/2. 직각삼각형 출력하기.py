# https://school.programmers.co.kr/learn/courses/30/lessons/120823?language=python3

def solution(n):
    answer = ""
    
    for i in range(1,n+1):
        for j in range(0,i):
            answer += "*"
        answer+= "\n"
    
    return answer
n = int(input())
print(solution(n))