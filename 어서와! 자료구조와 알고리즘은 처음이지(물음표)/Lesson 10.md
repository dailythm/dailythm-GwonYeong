# 양방향 연결리스트

-   한 쪽으로만 링크를 연결하지 말고 양쪽으로!
    -   다음 node로, 이전 node로 진행이 가능함.

```
class Node:
    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None
```

## 양방향 연결 리스트

리스트 처음과 끝에 dummy node를 두자.

-   데이터를 담고 있는 node들은 모두 같은 모양이 됨.

```
class DoublyLinkedList:
    def __init__(self, item):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None
```

---

## 리스트 순회

```
def traverse(self):
    result = []
    curr = self.head
    while curr.next.next:
        curr = curr.next
        result.append(curr.data)
    return result
```

<h2>역순회</h2>

```
def traverse(self):
    result = []
    curr = self.head
    while curr.prev.prev:
        curr = curr.next
        result.append(curr.data)
    return result
```

<h2>원소 삽입</h2>
newNode의 prev와 next를 잘 생각할 것.
삽입할 위치의 노드 앞과 뒤의 노드도 연결해야 함을 생각할 것.

<br>
<h2>특정 원소 찾기</h2>
입력받은 위치가 self.nodeCount //2 보다 큰 경우 head부터가 아닌 tail부터 찾도록 개선할 수 있겠음.

---

<h2>실습</h2>

역방향으로 리스트 순회하기

```
def reverse(self):
        tail = self.tail
        result = []
        while tail.prev.prev:
            result.append(tail.prev.data)
            tail = tail.prev

        return result
```

양방향 연결 리스트 노드 삽입

```
 def insertBefore(self, next, newNode):

        prev = next.prev
        prev.next = newNode
        newNode.prev = prev
        newNode.next = next
        next.prev = newNode
        self.nodeCount +=1

        return True
```

---

양방향 연결 리스트 노드 삭제

```
def popAfter(self, prev):

        curr = prev.next
        prev.next = curr.next
        curr.next.prev = prev
        self.nodeCount -=1
        return curr.data


    def popBefore(self, next):
        prev = next.prev
        prev.prev.next = next
        next.prev = prev.prev
        self.nodeCount -=1
        return prev.data


    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        result = self.popAfter(self.getAt(pos-1))
        return result
```

양방향 리스트의 결합

```
  def concat(self, L):
        self.tail.prev.next = L.head.next
        L.head.next.prev = self.tail.prev
        self.tail = L.tail
        self.nodeCount += L.nodeCount
```
