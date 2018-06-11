
import collections
from binarytree import BiTreeNode as Node

def iscbt(root):

    if not root:
        return True

    deque = collections.deque()
    deque.append(root)
    statu = 0

    while deque:
        node = deque.popleft()
        print(node.data, end=' ')

        if statu and (node.left or node.right):
            return False

        if node.left:
            deque.append(node.left)
        else:
            statu = 1
        if node.right:
            deque.append(node.right)
        else:
            statu = 1

    return True



def getexampletree():
    head = Node(6)
    head.parent = None
    head.left = Node(3)
    head.left.parent = head
    head.left.left = Node(1)
    head.left.left.parent = head.left
    head.left.left.right = Node(2)
    head.left.left.right.parent = head.left.left
    head.left.right = Node(4)
    head.left.right.parent = head.left
    head.left.right.right = Node(5)
    head.left.right.right.parent = head.left.right
    head.right = Node(9)
    head.right.parent = head
    head.right.left = Node(8)
    head.right.left.parent = head.right
    head.right.left.left = Node(7)
    head.right.left.left.parent = head.right.left
    head.right.right = Node(10)
    head.right.right.parent = head.right

    return head


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print(iscbt(root))

    root2 = getexampletree()
    print(iscbt(root2))

if __name__ == '__main__':
    main()
