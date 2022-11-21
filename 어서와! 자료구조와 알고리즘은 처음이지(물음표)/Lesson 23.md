# 힙(2)

## 최대 힙에서 원소의 삭제

1. 루트 노드의 제거 : 이것이 원소들 중 최댓값
2. 트리 마지막 자리 노드를 임시로 루트 노드의 자리에 배치
3. 자식 노드들과의 값 비교와 아래로, 아래로 이동.
   - 자식은 둘이 있을 수 있는데 어느쪽으로 이동해야 할까?

최대 힙에서 원소의 삭제는 가장 큰 값, 루트 노드만 삭제 가능함!!

1. 루트 노드를 삭제
2. 가장 마지막 자리 노드를 임시로 루트 노드의 자리에 배치.
3. 최대 힙의 성질에 맞게 노드를 이동시켜주기.

(최대 힙에서 원소의 삭제)

---

## 삭제 연산

(삭제 연산의 구현)
루트 노드를 삭제하고 가장 마지막 노드를 올리는 과정

(삭제 연산의 구현 2)
자기 자신이 최대값을 가지는 경우 재귀함수가 멈추게 될 것임.

- i로 받은 자신이 가장 큰 값이 아니라면 더 큰 값과 자리를 바꿔주는 것.

---

## 복잡도

- 자식 노드들과의 대소 비교 최대 회수 : 2 \* log n
- 최악 복잡도는 log n의 삭제 연산

```
class MaxHeap:

    def __init__(self):
        self.data = [None]


    def remove(self):
        if len(self.data) > 1:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop(-1)
            self.maxHeapify(1)
        else:
            data = None
        return data


    def maxHeapify(self, i):
        # 왼쪽 자식 (left child) 의 인덱스를 계산합니다.
        left =
i * 2

        # 오른쪽 자식 (right child) 의 인덱스를 계산합니다.
        right =
i * 2 + 1

        smallest = i
        # 왼쪽 자식이 존재하는지, 그리고 왼쪽 자식의 (키) 값이 (무엇보다?) 더 큰지를 판단합니다.
        if
left < len(self.data)
 and
self.data[smallest] < self.data[left]
:
            # 조건이 만족하는 경우, smallest 는 왼쪽 자식의 인덱스를 가집니다.

smallest = left

        # 오른쪽 자식이 존재하는지, 그리고 오른쪽 자식의 (키) 값이 (무엇보다?) 더 큰지를 판단합니다.
        if
right < len(self.data)
 and
self.data[smallest] < self.data[right]
:
            # 조건이 만족하는 경우, smallest 는 오른쪽 자식의 인덱스를 가집니다.

smallest = right

        if smallest != i:
            # 현재 노드 (인덱스 i) 와 최댓값 노드 (왼쪽 아니면 오른쪽 자식) 를 교체합니다.

self.data[i], self.data[smallest] = self.data[smallest], self.data[i]

            # 재귀적 호출을 이용하여 최대 힙의 성질을 만족할 때까지 트리를 정리합니다.
            self.maxHeapify(smallest)


def solution(x):
    return 0
```
