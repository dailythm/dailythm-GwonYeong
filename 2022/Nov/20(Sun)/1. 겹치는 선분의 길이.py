# https://school.programmers.co.kr/learn/courses/30/lessons/120876

def solution(lines):
    answer = 0
    min_num = lines[0][0]
    max_num = lines[0][1]
    for i in lines:
        min_num = min(min_num, i[0])
        max_num = max(max_num, i[1])
    
    for j in range(min_num, max_num +1):
        if lines[0][0] <= j < lines[0][1] and lines[1][0] <= j < lines[1][1]:
            answer +=1
        elif lines[1][0] <= j < lines[1][1] and lines[2][0] <= j < lines[2][1]:
            answer += 1
        elif lines[0][0] <= j < lines[0][1] and lines[2][0] <= j < lines[2][1]:
            answer += 1
            
    return answer