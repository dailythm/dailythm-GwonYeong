# https://school.programmers.co.kr/learn/courses/30/lessons/12969

a, b = map(int, input().strip().split(' '))
answer = ''
for i in range(b):
    for j in range(a):
        answer += '*'
    answer += '\n'
print(answer)