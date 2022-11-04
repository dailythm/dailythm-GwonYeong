# 연결 리스트가 힘을 발휘할 때

중간에 삽입하거나 중간의 자료를 삭제하거나

-   삽입과 삭제가 유연하다는 것이 가장 큰 장점
-   하지만 항상 맨 앞에서부터 찾아야 하기 때문에 매번 연산이 들어가야하는 단점.

---

# 조금 변형 된 연결 리스트

맨 앞에 더미 노드를 추가한 형태

```
class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = None
        self.head.next = self.tail
```

---

# 원소의 삽입

```
def insertAfter(self, prev, newNode):
    newNode.next = prev.next #삽입하기 전의 노드를 새로운 노드의 next로
    prev.next = newNode #삽입하기 전의 노드의 next를 새로운 노드로
    self.nodeCount += 1
    return true
```

1. pos 범위 조건 확인
2. pos == 1인 경우 head 뒤에 새 node
3. pos == nodeCount+1인 경우는 prev가 tail
4. 그렇지 않은 경우에는 prev의 위치를 찾기

---

# 원소의 삭제

1. prev가 마지막 node인 경우 (prev.next == None)

-   삭제할 node가 없음.
-   return None

2. 리스트 맨 끝의 node를 삭제

-   tail을 조정하기.

---

# 실습

```
 def popAfter(self, prev):
        if prev.next == None:
            return None
        curr = prev.next
        if curr.next == None:
            if self.nodeCount == 1:
                self.tail = None
            else:
                self.tail = prev


        prev.next = curr.next
        self.nodeCount -=1
        return curr.data



    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount  :
            raise IndexError


        prev = self.getAt(pos-1)
        return self.popAfter(prev)
```
