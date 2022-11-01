# Linked Lists 연결 리스트

배열, 선형 배열과 유사한 구조

## 추상적 자료구조

추상적: 내부 구현을 숨겨두고 밖에서 보이는 것을 제공

-   Data
    -   예: 정수, 문자열, 레코드 ...
-   A set of operations
    -   삽입, 삭제, 순회
    -   정렬, 탐색

## 기본적 연결 리스트

https://t1.daumcdn.net/cfile/tistory/99CEE2425CB7F7CB10

각 칸 하나를 Node라고 부르고

-   Data
-   Link(next)
    로 나누어짐.

Node 내의 데이터는 다른 구조로 이루어질 수 있음.

ex: 문자열, 레코드, 또 다른 연결리스트 등..

리스트의 맨 앞은 Head 가장 끝 원소는 Tail

전체 노드의 수를 구하고 Tail을 구해놓는 것이 편함.

Node 라는 클래스를 만들고 Data, Link를 이용해 인스턴스를 만듬.

```
class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None
```

---

## 연산 정의

1. 특정 원소 참조
2. 리스트 순회
3. 길이 걷어내기
4. 원소 삽입
5. 원소 삭제
6. 두 리스트 합치기

## 특정 원소 참조

```
def getAt(self, pos):
    if pos <= 0 or pos> self.nodeCount:
        return None
    i = 1
    curr = self.head
    while i < pos:
        curr = curr.next
        i += 1
    return curr
```

배열과 비교한 연결 리스트

|                | 배열        | 연결 리스트     |
| -------------- | ----------- | --------------- |
| 저장공간       | 연속한 위치 | 임의의 위치     |
| 특정 원소 지칭 | 매우 간편   | 선형탐색과 유사 |
|                | O(1)        | O(n)            |

---

실습

```
class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None
        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    def traverse(self):
        answer = []
        curr = self.head
        while 1:
            try:
                answer.append(curr.data)
                curr = curr.next

            except:
                return answer


# 이 solution 함수는 그대로 두어야 합니다.
def solution(x):
    return 0
```

## 코드 설명

curr 이라는 변수에 head 노드를 넣었습니다.

이후 try..except 를 사용하였는데 이는 curr이 None값이 되면 curr.data를 참조하는 과정에서 에러가 나는 것을 이용했습니다.

어쩌면 좋은 코드는 아니지만 짧고 간결하게 하는 목적에서는 사용할 만한 방식이라고 생각합니다.
