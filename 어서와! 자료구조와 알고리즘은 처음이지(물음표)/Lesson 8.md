# 연결 리스트 2

## node의 삽입과 삭제

---

## 연결 리스트 연산 - 원소의 삽입

```
def insertAt(selfm pos, newNode):
```

pos가 가리키는 위치에 (1 <= pos <= nodeCount + 1)
new Node를 삽입하고
성공 / 실패에 따라 True/ false를 리턴

삽입하려는 자리의 **왼쪽의 노드** 의 next를 삽입하는 노드로 향하게 하고

**삽입하려는 노드**의 next를 **오른쪽의 노드** 로 향하게 만든다.

```
def insertAt(self, pos, newNode):
    prev = self.getAt(pos-1)
    newNode.next = prev.next
    prev.next = newNode
    self.nodeCount += 1
```

### 예외 사항

1. 삽입하려는 위치가 리스트 맨 앞일 때

-   prev 없음
-   Head 조정이 필요함

2. 삽입하려는 위치가 리스트 맨 끝

-   Tail 조정 필요

또 빈 리스트에 삽입할 때는?

pos 가 1인 경우, pos가 self.nodeCount +1인 경우를 나누어서 처리할 수 있음.

---

## 연결 리스트 원소 삽입의 복잡도

맨 앞에 삽입 : O(1)

중간에 삽입 : O(n)

맨 끝에 삽입: O(1)

-   만약 pos가 self.nodeCount+1 이라면 그냥 꼬리에 넣어주면 되기 때문.

---

## 원소의 삭제

```
def popAt(self, pos):

```

pos가 가리키는 위치의 (1 <= pos <= nodeCount)

node를 삭제하고

그 node의 데이터를 리턴

삽입과 마찬가지의 예외사항, 복잡도를 가지고 있음.

---

## 두 리스트의 연결

L1의 tail이 L2의 head를 가리키게 만든다거나

self.tail.next = L2.head
self.tail = L2.tail

마찬가지로 배열이 빈 경우를 생각할 것.

---

실습
