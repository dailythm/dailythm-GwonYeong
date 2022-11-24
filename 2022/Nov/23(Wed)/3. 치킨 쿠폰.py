# https://school.programmers.co.kr/learn/courses/30/lessons/120884

def solution(chicken):
    coupon = 0
    service = 0
    idx = 0
    while chicken >= idx:
        if coupon == 10:
            service +=1
            chicken +=1
            coupon = 0
        coupon +=1
        idx+=1
    return service