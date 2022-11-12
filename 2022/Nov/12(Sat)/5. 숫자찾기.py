# https://school.programmers.co.kr/learn/courses/30/lessons/120904

def solution(num, k):
    num = str(num)
    k = str(k)
    print(num, k)
    for i in range(len(num)):
        if num[i] == k:
            return i+1
    return -1
        
    