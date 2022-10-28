# 정렬과 탐색

정렬 : 배열 안의 원소들을 정해진 규칙에 따라 재배치.

파이썬에서는

1. sorted() 를 이용(내장함수), 정렬된 새로운 리스트를 얻어냄.
2. sort() 리스트의 메서드, 해당 리스트를 정렬

```
L = [3,8,2,7,6,10,9]
print(sorted(L2)) # [2,3,6,7,8,9,10]
# L2 배열은 실질적으로 변하지 않음.
L.sort() #
# L2 배열을 실질적으로 정렬시킴.
```

경우에 따라 정렬의 순서를 반대로 하고 싶을 수 있는데 reverse = True 를 이용할 수 있음.

L2 = sorted(L, reverse = True)

L2.sort(reverse = True)

문자열로 이루어진 리스트의 경우 사전 순서를 따름. (문자열 길이가 길다고 큰 것이 아님!)

-   문자열을 길이 순서로 정렬하려면 정렬에 이용하는 key를 지정해서 사용.

```
L = ['abcd', 'xyz', 'spam']

sorted(L, key = lambda x: len(x))
```

---

정렬 - 키를 지정하는 또 다른 예시

L = [{'name' : 'John', score : 83} , {'name' : 'Paul', score : 98}]

L.sort(key(lambda x: x['score'] , reverse = True))
레코드들을 점수가 높은 순으로 정렬

---

## 탐색 알고리즘

### Linear Search 선형 탐색

앞에서 뒤로 하나씩 찾아가며 비교하는 방법.

리스트가 정렬되어 있어도 방법이 똑같음.

-   리스트의 길이에 비례하는 시간 소요 O(n)
-   최악의 경우: 모든 원소를 다 비교해 보아야 함.
    -   리스트에 존재하지 않거나 찾는 값이 가장 끝에 있거나.

### 이진탐색

-   탐색하려는 리스트가 정렬되어 있는 경우에만 사용 가능.
-   가장 중앙의 값과 찾는 값을 비교해 왼쪽, 오른쪽을 나누어 찾아가는 방법.

한 번 비교가 일어날 때 마다 리스트를 반씩 줄임.
O(log n)

---

## 실습

이진 탐색 구현.

-   배열이 빈 값인 경우를 생각하느라 시간이 오래걸림.

```
def binary(arr, left, right, target):
    middle = (left + right) // 2

    if(left >= right and arr[middle] != target):
        return -1
    if(arr[middle] == target):
        return middle
    if(arr[middle] > target):
        right = middle - 1
    else:
        left = middle + 1
    return binary(arr, left, right, target)
def solution(L, x):
    if(len(L) <= 0):
        return -1
    return binary(L, 0, len(L)-1, x)
```
