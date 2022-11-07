# Stacks

스택 : 자료를 보관할 수 있는 (선형) 구조

단, 넣을 떄에는 한 쪽에서 넣어주고 꺼낼 때는 같은 쪽에서 뽑아 꺼내주어야 함.

후입선출 LIFO

```
S = Stack()
S.push(A) # A를 스택에 삽입
S.push(B) # B를 스택에 삽입
r1 = S.pop() # 맨 위에 있던 B를 꺼내 r1에 넣어줌.
r2 = S.pop()
```

만약 비어있는 스택에서 데이터 원소를 꺼내려 한다면?
<br> => 스택 언더플로우

꽉 찬 스택에 데이터 원소를 넣으려 할 때
<br> => 스택 오버플로우

---

## 스택의 추상적 자료구조 구현

1. 배열(array)을 이용해 구현

-   파이썬 리스트와 메서드를 이용

2. 연결 리스트를 이용해 구현

-   양방향 연결리스트 이용

---

연산의 정의

-   size() : 현재 스택에 들어있는 데이터 원소의 수를 구함
-   isEmpty() : 현재 스택이 비어있는지 판단
-   push(x) : 데이터 원소 x를 스택에 추가
-   pop() : 스택의 맨 위에 저장된 데이터원소를 제거(반환)
-   peek() : 스택의 맨 위에 저장된 데이터 원소를 반환(제거하지 않음. 보기만 하는 것.)

---

배열을 이용한 구현

```
class ArrayStack:
    def __init__(self):
        self.data = [] # 빈 스택을 초기화

    def size(self):
        return len(self.data) # 스택의 크기를 리턴

    def isEmpty(self):
        return self.size() == 0 # 스택이 비어있는지 판단

    def push(self, item):
        self.data.append(item) #데이터 원소를 추가

    def pop(self):
        return self.data.pop() # 데이터 원소 삭제

    def peek(self):
        return self.data[-1]
```

---

양방향 연결 리스트를 이용해 구현
![양방향 연결 리스트를 이용해 스택 구현](https://user-images.githubusercontent.com/71562311/200171615-98ec1251-cf43-4df1-a850-8968c79b7cd5.PNG)

---


스택 라이브러리를 이용해 구현

```
from pythonds.baic.stack import Stack
S = Stack()
dir(S)
#이미 만들어진 스택의 메서드를 확인할 수 있음.
```

---

## 활용

수식의 괄호 유효성 검사

-   올바른 수식

    -   (A + B)
    -   {(A + B) \* C}
    -   {(A + B) \* (C + D)}

-   올바르지 않은 수식
    -   (A + B
    -   A + B)
    -   [(A + B) \* (C + D)}

알고리즘 설계 : 수식을 왼쪽부터 한 글자씩 읽어서

-   여는 괄호 : ( 또는 { 또는 [를 만나면 스택에 푸시
-   닫는 괄호 : ) 또는 } 또는 ] 를 만나면
    -   스택이 비어 있으면 올바르지 않은 수식
    -   스택에서 pop, 쌍을 이루는 여는 괄호인지 검사
        -   맞지 않으면 올바르지 않은 수식
-   끝까지 검사한 후 스택이 비어 있어야 올바른 수식

---

```
def solution(expr):
    match = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    S = ArrayStack()
    for c in expr:
        if c in '({[':

            S.push(c)

        elif c in match:
            if S.isEmpty():
                return False
            else:
                t = S.pop()

                if t !=match[c]:
                    return False
    return S.isEmpty()
```
