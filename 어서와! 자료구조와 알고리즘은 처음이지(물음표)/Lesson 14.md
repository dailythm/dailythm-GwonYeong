# Queue

자료를 보관할 수 있는 (선형) 구조

단, 넣을 떄에는 한 쪽 긑에서 밀어 넣고 꺼낼 때는 반대 쪽에서 뽑아 꺼내야 하는 제약이 있음.

enqueue : 한 쪽 끝에서 밀어넣는 연산
dequeue : 한 쪽 끝에서 꺼내는 연산

줄을 서는 느낌.

Q = Queue() # 빈 큐를 선언

Q.enqueue(A) # A를 큐에 넣음

Q.enqueue(B) # B를 큐에 넣음

r1 = Q.dequeue() # 먼저 들어온 A를 꺼냄.

r2 = Q.dequeue() # 나중에 들어온 B를 꺼냄.

---

큐의 추상적 자료구조 구현

1. 배열을 이용해 구현

- 파이썬 이스트와 메서드를 사용

2. 연결 리스트를 이용해 구현

- 이전 강의에서 마련한 양방향 연결 리스트 이용

큐의 주상적 자료구조 구현

- size() : 현재 큐에 들어 있는 데이터 원소의 수
- isEmpty() : 현재 구가 비어있는지 판단
- enqueue(x) : 데이터 원소 x를 큐에 추가
- dequeue() : 큐의 맨 앞에 저장된 데이터 원소를 제거 (반환)
- peek() : 큐의 맨 앞에 저장된 데이터 원소를 반환(제거 X)

선입선출!!

---

배열로 구현하면?
```
Class ArrayQueue:
    def __init__(self):
        self.data = [] # 빈 큐를 초기화
    def size(self):
        return len(self.data) # 큐의 크기
    def isEmpty(self):
        return self.size() == 0 # 큐가 비어있는지
    def enqueue(self, item):
        self.data.append(item) # 데이터 원소를 추가
    def dequeue(self):
        return self.data.pop(0) # 데이터 원소를 삭제
    def peek(self):
        return self.data[0]
---

배열로 구현한 큐의 연산 복잡도

dequeue() 는 O(n)이며 (pop 같은 경우 원소를 제거 한 후 뒤에 있는 원소를 앞으로 한 칸씩 당겨주어야 하기 때문)

나머지는 O(1)

---
from pythonds.basic.queue()