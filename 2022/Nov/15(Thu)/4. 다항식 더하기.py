# https://school.programmers.co.kr/learn/courses/30/lessons/120863#

def solution(polynomial):
    answer = ''
    s = polynomial.split(' ')
    x = 0
    num = 0
    for i in s:
        if 'x' in i:
            try:
                
                x += int(i[:-1])
            except:
            
                x += 1
        elif i != '+':
            num += int(i)
    if x != 0:
        if x !=1:
            answer += str(x) + 'x'
        else : 
            answer += 'x'
        if num != 0:
            answer +=   ' + ' + str(num)
            return answer
        else :
            return answer
    
    return str(num)