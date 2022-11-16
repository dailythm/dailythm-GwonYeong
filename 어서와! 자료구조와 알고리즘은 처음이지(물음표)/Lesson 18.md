# 이진 트리

## 이진 트리의 추상적 자료구조

- 연산의 정의
  - size() 현재 트리에 포함되어 있는 노드의 수를 구함
  - depth() 현재 트리의 깊이를 구함
  - traversal 정해진 순서대로 트리를 순회
![이진트리](https://user-images.githubusercontent.com/71562311/202320239-714efdd0-414a-4f14-8519-8bc66064bd90.PNG)

노드

left와 right를 하나씩 가짐.

Node

- Data
- Left
- Right

같은 식으로 인스턴스를 생성

---

size 같은 메소드는 재귀함수로 구현 가능함.


![이진트리 구현](https://user-images.githubusercontent.com/71562311/202320124-2a6edf96-6ed9-4441-806e-329bb17ab54a.PNG)

self.root 가 있다면 사이즈를 구할 수 있고 없다면 0을 반환하면 됨.

---

depth
![depth](https://user-images.githubusercontent.com/71562311/202320146-dad48009-de75-4d36-b6e9-3ac733dd49a7.PNG)

---

## Traversal

깊이 우선 순회

- 중위 순회
  
![중위 순회](https://user-images.githubusercontent.com/71562311/202320156-18300ae1-59a9-4df0-b319-e721c0b01b89.PNG)

```
class Node:
  def inorder(self):
    traversal = []
    if self.left:
      traversal += self.left.inorder()
    traversal.append(self.data)
    if self.right:
      traversal += self.right.inorder()
    return traversal
```

왼쪽 -> 자신 -> 오른쪽 순서

- 전위 순회

자신 => 왼쪽 => 오른쪽

- 후위 순회

왼쪽 => 오른쪽 => 자신

넓이 우선 순회

```
class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


    def size(self):
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l + r + 1


    def depth(self):
        l = self.left.depth() if self.left else 0
        r = self.right.depth() if self.right else 0
        return max(l, r) + 1


class BinaryTree:

    def __init__(self, r):
        self.root = r

    def size(self):
        if self.root:
            return self.root.size()
        else:
            return 0


    def depth(self):
        if self.root :
            return self.root.depth()
        else: return 0


def solution(x):
    return 0
```

```
class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self.data)
        if self.right:
            traversal += self.right.inorder()
        return traversal


    def preorder(self):
        traversal = []
        traversal.append(self.data)
        if self.left:
            traversal += self.left.preorder()

        if self.right:
            traversal += self.right.preorder()
        return traversal


class BinaryTree:

    def __init__(self, r):
        self.root = r


    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []


    def preorder(self):
        if self.root:
            return self.root.preorder()
        else:
            return []


def solution(x):
    return 0
```

```
class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self.data)
        if self.right:
            traversal += self.right.inorder()
        return traversal


    def postorder(self):
        traversal = []
        if self.left:
            traversal += self.left.postorder()
        if self.right:
            traversal += self.right.postorder()
        traversal.append(self.data)

        return traversal


class BinaryTree:

    def __init__(self, r):
        self.root = r


    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []


    def postorder(self):
        if self.root:
            return self.root.postorder()
        else:
            return []


def solution(x):
    return 0
```
