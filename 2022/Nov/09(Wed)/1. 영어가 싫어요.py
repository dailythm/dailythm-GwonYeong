# https://school.programmers.co.kr/learn/courses/30/lessons/120894?language=python3

def solution(numbers):
    answer = 0
    dictionary = {
        'zero' : '0',
        'one' : '1',
        'two' : '2',
        'three' : '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',
        'seven' : '7',
        'eight': '8',
        'nine' : '9'
    }
    for i in dictionary:
        
        while i in numbers:
            numbers = numbers.replace(i, dictionary[i])    
    answer = int(numbers)
    return answer