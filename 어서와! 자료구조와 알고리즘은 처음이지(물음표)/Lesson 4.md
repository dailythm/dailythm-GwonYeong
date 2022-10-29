# Recursive Functions 재귀함수

자신을 호출하는 함수.

---

## 이진트리

왼쪽 트리에는 자신보다 작은 노드, 오른쪽에는 자신보다 큰 노드.

이러한 규칙이 모든 노드에게 적용된다면? 재귀함수를 사용할 수 있음.

---

## 1 ~ n 까지의 합 구하기

```
def recursive(n):
    if(n <=1):
        return n
    else return n +recursive(n-1)
recursive(10) # 55
```

재귀함수는 반드시 호출이 끝나는 경우를 만들어 주어야 함.

---

실습

인자로 0 또는 양의 정수인 x 가 주어질 때, Fibonacci 순열의 해당 값을 구하여 반환하는 함수 solution() 을 완성하세요.

Fibonacci 순열은 아래와 같이 정의됩니다.
F0 = 0
F1 = 1
Fn = Fn - 1 + Fn - 2, n >= 2

재귀함수 작성 연습을 의도한 것이므로, 재귀적 방법으로도 프로그래밍해 보고, 반복적 방법으로도 프로그래밍해 보시기 바랍니다.

def recursive(num1, num2, x):
if x <= 0 :
return num1
return recursive(num2, num1 + num2 , x-1)
def solution(x):

    return recursive(0, 1, x)
