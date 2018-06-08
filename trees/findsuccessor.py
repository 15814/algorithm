


class Node(object):
    """docstring for Node."""
    def __init__(self, data = None, left = None, right = None, parent = None):
        super(Node, self).__init__()
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent



def findsuccessor(targetnode):
    if not targetnode:
        return Node()

    if targetnode.right:
        node = targetnode.right
        while node.left:
            node = node.left
        return node
    elif targetnode.parent.left == targetnode:
        return targetnode.parent

    else:
        node = targetnode
        parent = targetnode.parent
        while parent and parent.left != node:
            node = parent
            parent = parent.parent

        if parent:
            return parent
        else:
            return Node()


def test():
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

    test = head.left.left
    print(test.data , " next: " , findsuccessor(test).data)
    test = head.left.left.right
    print(test.data , " next: " , findsuccessor(test).data)
    test = head.left
    print(test.data , " next: " , findsuccessor(test).data)
    test = head.left.right
    print(test.data , " next: " , findsuccessor(test).data)
    test = head.left.right.right
    print(test.data , " next: " , findsuccessor(test).data)
    test = head
    print(test.data , " next: " , findsuccessor(test).data)
    test = head.right.left.left
    print(test.data , " next: " , findsuccessor(test).data)
    test = head.right.left
    print(test.data , " next: " , findsuccessor(test).data)
    test = head.right
    print(test.data , " next: " , findsuccessor(test).data)
    test = head.right.right # 10's next is null
    print(test.data , " next: " , findsuccessor(test).data)

    import binarytree
    binarytree.preorder_unrecur(head)
    binarytree.inoreder_unrecur2(head)

    binarytree.levelorder(head)

def main():
    test()



if __name__ == '__main__':
    main()
