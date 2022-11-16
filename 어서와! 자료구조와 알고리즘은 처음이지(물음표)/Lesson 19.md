# 이진트리

## 넓이 우선 순회

- 원칙 : 수준이 낮은 노드를 우선으로 방문
- 수준 == Level
- 같은 수준의 노드들 사이에는
  - 부모 노드의 방문 순서에 따라 방문
  - 왼쪽 자식 노드를 오른쪽 자식보다 먼저 방문
- 재귀적 방법이 적합할까? (X)

---

- 한 노드를 방문했을 때
  - 나중에 방문할 노드들을 순서대로 기록해 두어야 함.
    - 큐를 이용??

```
class ArrayQueue:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]


class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, r):
        self.root = r


    def bft(self):
        q = ArrayQueue()
        result = []
        if self.root:

            q.enqueue(self.root)
        while q.size():
            curr = q.dequeue()
            result.append(curr.data)
            if curr.left:
                q.enqueue(curr.left)
            if curr.right:
                q.enqueue(curr.right)


        return result


def solution(x):
    return 0
```
