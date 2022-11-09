# https://school.programmers.co.kr/learn/courses/30/lessons/120896
def solution(s):
    answer = ''
    s = list(s)
    s.sort()
    for i in range(97 , 123):
       
        if s.count(chr(i)) ==1:
            answer += chr(i)
    return answer