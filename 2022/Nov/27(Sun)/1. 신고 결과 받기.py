# https://school.programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    dictionary = {}
    for user in report:
        user = user.split(' ')
        try:
            if user[0] not in dictionary[user[1]]:
                
                dictionary[user[1]] += [user[0]]
        except:
            dictionary[user[1]] = [user[0]]
    for i in dictionary:
        if len(dictionary[i]) >= k:
            for j in dictionary[i]:
                answer[id_list.index(j)] += 1
        print(len(dictionary[i]))
    return answer