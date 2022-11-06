# https://school.programmers.co.kr/learn/courses/30/lessons/120850

def solution(my_string):
    answer = []
    for i in my_string:
        try:
            
            num =int(i)
            answer.append(num)
        except:
            continue
    
    answer.sort()
    
    return answer