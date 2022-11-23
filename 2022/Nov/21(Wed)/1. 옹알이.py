# https://school.programmers.co.kr/learn/courses/30/lessons/120956?language=python3

def solution(babbling):
    answer = 0
    for string in babbling:
        for word in ["aya", "ye", "woo", "ma"]:
            
            string = string.replace(word,'0')
        
        if string.count('0') == len(string):
            answer +=1
    
    return answer