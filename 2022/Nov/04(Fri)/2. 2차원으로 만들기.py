# https://school.programmers.co.kr/learn/courses/30/lessons/120842

def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        temp = []
        for j in range(i, i +n):
            temp.append(num_list[j])
        answer.append(temp)
    return answer