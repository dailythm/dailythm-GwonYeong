# 재귀 알고리즘 응용

효율적인 측면에선 반복문에 비해 약점을 가진다는 것을 기억할 것.

---

## 조합의 수 계산

문제 : n 개의 서로 다른 원소에서 m 개를 택하는 경우의 수 (n , m)

```
from math import factorial as f
def combi(n,m):
    return f(n) / (f(m) * f(n - m))
```

이를 재귀적 방법으로 구현하려면

(n , m) == (n - 1, m) + (n - 1, m - 1)

```
def combi(n,m):
    if n == m:
        return 1
    elif m == 0:
        return 1
    else:
        return combi(n-1,m) + (combi( n-1, m-1))
```

재귀 알고리즘은 함수를 여러번 호출하고 return이 많기 때문에 효율성 면에서는 좋지 않음.

---

## 하노이의 탑 (그켬)

---
