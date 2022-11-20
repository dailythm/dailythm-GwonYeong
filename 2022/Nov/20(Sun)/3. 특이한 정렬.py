# https://school.programmers.co.kr/learn/courses/30/lessons/120880

def solution(numlist, n):
    numlist.sort(reverse=True)
    numlist.sort(key=lambda x:abs(x-n))
    return numlist