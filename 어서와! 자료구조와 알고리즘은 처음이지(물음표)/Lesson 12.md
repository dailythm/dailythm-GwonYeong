# 중위 표기법과 후위 표기법

중위 표기법(infix notation)
<br> (A + B) * (C + D)<br>

A + B를 계산한 뒤 C + D를 계산, 두 값을 곱함

* 연산자가 피연산자들의 사이에 위치

후위 표기법(postfix notation)
<br> AB+CD+*

* 연산자가 피연산자들의 뒤에 위치

앞에 나온 연산자부터 차례대로 계산함.

괄호도 필요 없음.

---

## 스택을 이용한 중위 표현식 -> 후위 표현식

중위 : A * B + C    후위 : AB*C+

1. 한 글자씩 살펴보고 피연산자라면 결과에 출력
2. 연산자라면 일단 스택에 push

2 - 1. 스택이 비어있지 않은 상태에서 연산자를 만났다면 현재 만난 연산자와 스택에 있는 연산자를 비교해 스택의 연산자가 우선순위가 높다면 스택 pop
<br>이후 스택에 우선순위가 낮은 연산을 push

2 - 2. 스택이 비어있지 않은 상태에서 연산자를 만났다면 현재 만난 연산자와 스택에 있는 연산자를 비교해 스택의 연산자가 우선순위가 낮다면 스택에 push

---

(+, +같은)동일 연산자라면 출력해주고 만난 연산자를 스택에 push


---
## 괄호의 처리
중위 ( A + B ) * C

여는 괄호를 먼저 스택에 넣고 닫는 괄호를 만나면 스택에서 pop
<br> 여는 괄호가 나올 때 까지

---

## 알고리즘의 설계
중위 표현식을 왼쪽부터 한 글자씩 읽어서 

    피연산자면 그냥 출력
    '(' 이면 스택에 push
    ')' 이면 '(' 가 나올 때까지 스택에서 pop, 출력
    연산자이면 스택에서 이보다 높(거나 같)은 우선순위 것들을 pop, 출력
        그리고 이 연산자는 스택에 push
스택에 남아 있는 연산자는 모두 pop, 출력


def solution(S):
    opStack = ArrayStack()
    answer = ''
    for i in S:
        if i in prec:
            if prec[i] == 1:
                opStack.push
                continue
            else:
                if prec[i] <= opStack:
                    answer+=opStack.pop()
        elif prec[i] == ')':
                while opStack.peek() != '(':
                    answer += opStack.pop()
                opStack.pop()







