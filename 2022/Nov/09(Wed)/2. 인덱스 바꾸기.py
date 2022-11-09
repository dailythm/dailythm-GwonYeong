# https://school.programmers.co.kr/learn/courses/30/lessons/120895

def solution(my_string, num1, num2):
        
    my_string = list(my_string)
    temp = my_string[num1]
    my_string[num1] = my_string[num2 ]
    my_string[num2 ] = temp
    my_string = ''.join(my_string)
    return my_string