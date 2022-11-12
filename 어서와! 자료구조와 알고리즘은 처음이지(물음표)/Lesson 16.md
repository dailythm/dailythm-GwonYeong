# 우선순위 큐

데이터 원소들의 우선순위가 정해져있어 FIFO 방식을 따르지 않고 우선순위에 따라 큐에서 빠져나오는 방식.

예시:
<br>작은 수가 우선순위가 높다고 가정할 때

Enqueue
<br>6, 7, 3, 2

Dequeue를 하면
<br>2, 3, 6, 7 순서로 빠져나오는 것.

우선순위 큐 활용

- 운영체제의 CPU 스케줄러(우선순위가 높은 프로세스를 먼저 처리)

서로다른 두 가지 방식이 가능

1. Enqueue 할 때 우선순위 순서를 유지하도록

2. Dequeue 할 때 우선순위 높은 것을 선택

기본적으로 1이 유리함.

서로 다른 두 가지 방법:

1. 선형 배열
2. 연결 리스트

연결 리스트는 중간에 삽입하는 것이 유연하기 때문에 연결 리스트가 시간측에서 유리함.

하지만 공간측에서 보면 선형 배열이 유리함을 가짐.

대부분 시간이 유리한 것을 우선으로 채택하기 때문에 연결 리스트가 많이 사용된다고 볼 수 있음.

---

```
def enqueue(self, x):
        newNode = Node(x)
        curr =
self.queue.head

        while curr.next != self.queue.tail and newNode.data < curr.next.data:
            curr = curr.next
        self.queue.insertAfter(curr, newNode)
```
