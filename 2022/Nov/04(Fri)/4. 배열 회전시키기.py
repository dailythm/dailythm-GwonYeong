# https://school.programmers.co.kr/learn/courses/30/lessons/120844

def solution(numbers, direction):
    
    if direction == "right":
        pop = numbers.pop()
        numbers.insert(0, pop)
    else :
        pop = numbers.pop(0)
        numbers.append(pop)
        
    
    return numbers