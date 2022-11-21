# 이진탐색 트리 2

이진 탐색 트리에서 원소 삭제

1. key를 이용해 노드를 찾는다.

   - 해당 키의 노드가 없으면 삭제할 것이 없음.
   - 노드를 찾으면 찾은 노드의 부모노드를 알고 있으면 삭제할 수 있음.

2. 찾은 노드를 제거하고도 이진 탐색 트리 성질을 만족하도록 트리의 구조를 정리해야함.

## 인터페이스의 설계

![인터페이스의 설계](https://user-images.githubusercontent.com/71562311/202897964-5c35e3aa-3e67-4d95-908b-31a7181480f2.PNG)

(인터페이스의 설계)

삭제할 노드가 있으면 삭제를 한 뒤 트리를 정리해주고 True 반환

없으면 False반환

---

이진탐색 트리 구조 유지

1. 삭제되는 노드가 leaf(자식이 없는) 노드인 경우
   - 그냥 그 노드를 없애면 됨.
     - 부모 노드의 링크를 조정
2. 자식을 하나 가지는 경우
   - 삭제되는 노드 자리에 그 자식을 대신 배치
     - 자식이 왼쪽에 있는지 오른쪽에 있는지를 판단해 배치
     - 부모 노드의 링크를 조정
3. 자식을 둘 가지고 있는 경우
   - 삭제되는 노드보다 바로 다음 큰 키를 가지는 노드를 찾아 그 노드를 삭제되는 노드 자리에 대신 배치하고 이 노드를 대신 삭제
  
![자식 세어보기](https://user-images.githubusercontent.com/71562311/202897969-bce8b86c-95f9-464b-8ecb-1d4fce4e6770.PNG)



일단 자식 수를 세어 경우의 수를 나누기

1. leaf 노드의 삭제

   - 삭제하려는 노드가 부모의 왼쪽 노드인 경우
   - 삭제하려는 노드가 부모의 오른쪽 노드인 경우
   - 그냥 그 노드만 삭제!

     - 삭제하려는 노드가 root node라면? self.root = None 같은 식으로 가야할 것임.

2. 자식이 하나인 노드의 삭제
   ![자식이 하나인 노드 삭제](https://user-images.githubusercontent.com/71562311/202897976-5ef07b30-f19c-4ce2-b0c6-f3aa37bcdec2.PNG)


자식을 삭제하려는 노드에 넣어주면 됨.

- 삭제되는 노드가 root라면 root의 자식을 root로 만들어 주어야 함.

3. 자식이 둘인 노드의 삭제
   ![자식이 둘인 노드 삭제](https://user-images.githubusercontent.com/71562311/202897984-36cd3bd3-af7f-4101-9d6b-023d43e074af.PNG)


삭제하려는 노드보다 한 단계 높은 노드의 자리를 찾음.

찾은 노드를 Success 의 S로, 부모노드를 P로 지정

이후 삭제하려는 노드자리에 S노드를 넣고 기존에 있던 S노드를 삭제.

---

이진 탐색 트리가 별로 효율적이지 못한 경우

![이진 탐색 트리가 별로 효율적이지 못한 경우](https://user-images.githubusercontent.com/71562311/202897996-61ce56da-c649-45b4-88d4-1f2d26b5c1c2.PNG)

한 쪽에 몰려있어 링크드 리스트보다 못한 경우
```
class Node:

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None


    def insert(self, key, data):
        if key < self.key:
            if self.left:
                self.left.insert(key, data)
            else:
                self.left = Node(key, data)
        elif key > self.key:
            if self.right:
                self.right.insert(key, data)
            else:
                self.right = Node(key, data)
        else:
            raise KeyError('Key %s already exists.' % key)


    def lookup(self, key, parent=None):
        if key < self.key:
            if self.left:
                return self.left.lookup(key, self)
            else:
                return None, None
        elif key > self.key:
            if self.right:
                return self.right.lookup(key, self)
            else:
                return None, None
        else:
            return self, parent


    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()
        return traversal


    def countChildren(self):
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count


class BinSearchTree:

    def __init__(self):
        self.root = None


    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)


    def lookup(self, key):
        if self.root:
            return self.root.lookup(key)
        else:
            return None, None


    def remove(self, key):
        node, parent = self.lookup(key)
        if node:
            nChildren = node.countChildren()
            # The simplest case of no children
            if nChildren == 0:
                # 만약 parent 가 있으면
                # node 가 왼쪽 자식인지 오른쪽 자식인지 판단하여
                # parent.left 또는 parent.right 를 None 으로 하여
                # leaf node 였던 자식을 트리에서 끊어내어 없앱니다.
                if parent:
                    if parent.left == node:
                        parent.left = None
                    else:
                        parent.right = None
                # 만약 parent 가 없으면 (node 는 root 인 경우)
                # self.root 를 None 으로 하여 빈 트리로 만듭니다.
                else:
                    self.root = None
            # When the node has only one child
            elif nChildren == 1:
                # 하나 있는 자식이 왼쪽인지 오른쪽인지를 판단하여
                # 그 자식을 어떤 변수가 가리키도록 합니다.
                if node.left:
                    temp = node.left

                else:
                    temp = node.right
                # 만약 parent 가 있으면
                # node 가 왼쪽 자식인지 오른쪽 자식인지 판단하여
                # 위에서 가리킨 자식을 대신 node 의 자리에 넣습니다.
                if parent:
                    if parent.left == node:
                        parent.left = temp
                    else :
                        parent.right = temp
                # 만약 parent 가 없으면 (node 는 root 인 경우)
                # self.root 에 위에서 가리킨 자식을 대신 넣습니다.
                else:
                    self.root = temp

            # When the node has both left and right children
            else:
                parent = node
                successor = node.right
                # parent 는 node 를 가리키고 있고,
                # successor 는 node 의 오른쪽 자식을 가리키고 있으므로
                # successor 로부터 왼쪽 자식의 링크를 반복하여 따라감으로써
                # 순환문이 종료할 때 successor 는 바로 다음 키를 가진 노드를,
                # 그리고 parent 는 그 노드의 부모 노드를 가리키도록 찾아냅니다.
                while successor.left:
                    parent = successor
                    successor  = successor.left
                # 삭제하려는 노드인 node 에 successor 의 key 와 data 를 대입합니다.
                node.key = successor.key
                node.data = successor.data
                # 이제, successor 가 parent 의 왼쪽 자식인지 오른쪽 자식인지를 판단하여
                # 그에 따라 parent.left 또는 parent.right 를
                # successor 가 가지고 있던 (없을 수도 있지만) 자식을 가리키도록 합니다.
                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right

            return True

        else:
            return False


    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []


def solution(x):
    return 0
```
