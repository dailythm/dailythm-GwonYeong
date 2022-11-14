# 트리

스택, 큐가 1차원의 구조라면 트리는 2차원의 구조

트리 : 정점, 간선을 이용해 데이터의 배치 형태를 추상화한 자료구조

실제 나무가 뿌리부터 이파리로 뻗어나가는 모양에서 나온 이름!
![트리](https://user-images.githubusercontent.com/71562311/201645970-7042c28f-5da2-4fbd-b231-800a3d9ba65b.PNG)

![컴퓨터 트리](https://user-images.githubusercontent.com/71562311/201645983-d8d002c9-7eb2-4c3c-a72a-16a27222bd3a.PNG)



가장 위의 Root(A)노드

밑에있는 GHJEK는 리프 노드

그 외는 내부노드

---

부모와 자식 노드

- 노드 D는 노드 GHJ의 부모노드
- 노드 E는 노드 C의 자식

노드 GHJ는 서로 형제(sibling)

조상(ancestor): 부모의 부모 이상(모두)

후손(descendant) : 자식의 자식 이상(모두)

---

노드의 수준

- A는 Level 0 (누군가는 1부터 시작하기도 함.)
- BC는 Level 1
- ...

트리의 높이 :

트리의 높이 = 최대수준(GHJK가 Level 3) + 1 == 4

부분 트리: 어느 한 노드를 기점으로 있는 자식들
<br> C를 기준으로 한다면 E, FK를 부분트리로 가지는 것.

노드의 차수 : 자식의 수와 같음

- A는 BC를 자식으로 가지므로 차수가 2가 됨.
- GHJEK는 차수가 0임.

---

## 이진트리

모든 차수가 2이하인 트리
![이진 트리](https://user-images.githubusercontent.com/71562311/201646005-f003e683-1646-4c85-ac10-9b3cad1002cb.PNG)



이진트리는 재귀적으로 정의할 수 있음.

루트노드 + 왼쪽 서브트리 + 오른쪽 서브트리
(왼쪽과 오른쪽 서브트리 또한 이진트리)

- 빈 트리이거나! (재귀를 멈출 경우의 수를 위해서)

---

## 포화 이진 트리

모든 레벨에서 노드들이 모두 채워져 있는 이진트리
![포화 이진 트리](https://user-images.githubusercontent.com/71562311/201646022-a7036bd2-02b1-4dc6-83f6-d3912c527b70.PNG)



높이가 k라면 노드의 개수가 2^k -1 인 이진트리

---

## 완전 이진 트리
![완전 이진 트리](https://user-images.githubusercontent.com/71562311/201646032-f6fa4ce1-2927-479a-82d3-26670c938da5.PNG)



포화 이진 트리는 아니지만 왼쪽부터 빈틈없이 채워진 트리

실습
https://school.programmers.co.kr/learn/courses/57/lessons/13792
