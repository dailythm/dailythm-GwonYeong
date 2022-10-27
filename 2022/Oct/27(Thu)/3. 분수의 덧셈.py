# https://school.programmers.co.kr/learn/courses/30/lessons/120808

import math
def solution(denum1, num1, denum2, num2):
    answer = [(denum1 * num2)+ (denum2 * num1), num1 * num2 ]
    gcd = math.gcd(answer[0], answer[1])
    answer = [answer[0] / gcd, answer[1] / gcd]
    return answer

