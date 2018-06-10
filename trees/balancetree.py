





def isbalance(root):
    if root:
        leftval, lefthigh = isbalance(root.left)
        if not leftval:
            return (False,0)
        rightval, righthigh = isbalance(root.right)
        if not rightval:
            return (False,0)

        if abs(lefthigh-righthigh) > 1:
            return (False,0)
        else:
            return (True, max(lefthigh,righthigh)+1 )

    else:
        return (True,0)










def main():
    import binarytree
    from binarytree import BiTreeNode as Node

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print(isbalance(root))












if __name__ == '__main__':
    main()
