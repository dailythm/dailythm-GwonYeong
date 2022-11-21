# 힙

- 이진 트리의 한 종류 (binary heap이라고도 부름)

1. 루트 노드가 언제나 최댓값 또는 최솟값을 가짐.
   - 최대 힙, 최소 힙
2. 완전 이진 트리여야 함!


![최대 힙의 예](https://user-images.githubusercontent.com/71562311/202898040-11764381-b2bb-4d18-86ac-a63dcbfd35e1.PNG)

재귀적으로도 정의 됨.

(어느 노드를 루트로 하는 서브트리도 모두 최대 힙!)

---

## 이진 탐색 트리와 비교

1. 원소들은 완전히 크기 순으로 정렬되어 있는가?
2. 특정 키값을 가지는 원소를 빠르게 검색할 수 있는가?
3. 부가의 제약 조건은 어떤 것인가?

---

## 배열을 이용한 이진 트리의 표현


![데이터 표현의 설계](https://user-images.githubusercontent.com/71562311/202898043-d25c45df-d576-4790-8f6d-a95d7e011b85.PNG)

완전 이진트리를 만족하기 때문에 배열로 표현하는 것이 나쁘지 않은 방법인 것임.

![최대 힙에 원소 삽입](https://user-images.githubusercontent.com/71562311/202898054-ed70eebe-ebfd-413f-bf14-f52c339f889a.PNG)


2. 부모 노드와 키 값을 비교하여 위로, 위로 이동

- 부모는 삽입하는 노드보다 값이 커야하니까.

최대 힙에 원소 삽입 복잡도는 log n

```
class MaxHeap:

    def __init__(self):
        self.data = [None]


    def insert(self, item):
        self.data.append(item)
        index = len(self.data) - 1

        while index > 1:
            parent = index // 2
            if self.data[index] > self.data[parent]:
                self.data[index], self.data[parent] = self.data[parent], self.data[index]
                index = parent
            else:
                break



def solution(x):
    return 0
```
