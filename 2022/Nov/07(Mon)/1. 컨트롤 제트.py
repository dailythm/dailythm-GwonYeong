def solution(s):
    answer = 0
    s = s.split(" ")
    try:
        while 1:
            
            s.remove(s[s.index('Z') -1])
            s.remove(s[s.index('Z')])
    except:
        pass
   
    for i in s:
        answer += int(i)
    return answer