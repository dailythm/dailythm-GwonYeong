# 후위 표기 수식 계산

AB+CD+\*

```
후위 표현식을 왼쪽부터 한 글자씩 읽어서
    피연산자이면 스택에 push
    연산자를 만나면 스택에서 pop -> (1), 도 pop -> (2)
        (2)연산(1) 을 계산 후 이 결과를 스택에 push
수식의 끝에 도달하면 스택에서 pop(계산의 결과)
```

```
def solution(S):
    opStack = ArrayStack()
    answer = ''

    for s in S:
        if s.isalpha():
            answer += s
        elif s == '(':
            opStack.push(s)
        elif s == ')':
            while not opStack.isEmpty():
                op = opStack.pop()
                if op == '(':
                    break
                else:
                    answer += op
        else:
            if not opStack.isEmpty():
                while not opStack.isEmpty():
                    if prec[opStack.peek()] >= prec[s]:
                        answer += opStack.pop()
                    else:
                        break
                opStack.push(s)
            else:
                opStack.push(s)

    while not opStack.isEmpty():
        answer += opStack.pop()


    return answer

```

```

```
