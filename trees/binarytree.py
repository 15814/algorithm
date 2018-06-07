
class BiTreeNode(object):
    """docstring for Node."""

    def __init__(self, data = None):
        super(BiTreeNode, self).__init__()
        self.data = data
        self.left = None
        self.right = None


class BiTree(object):
    """docstring for Tree."""

    def __init__(self, data = None):
        super(BiTree, self).__init__()
        self.root = BiTreeNode(data)


    def addchild(self, left = None, right = None):

        pass


    def exampletree(self):
        self.root.data = 5
        self.root.left = BiTreeNode(3)
        self.root.right = BiTreeNode(8)
        self.root.left.left = BiTreeNode(2)
        self.root.left.right = BiTreeNode(4)
        self.root.left.left.left = BiTreeNode(1)
        self.root.right.left = BiTreeNode(7)
        self.root.right.left.left = BiTreeNode(6)
        self.root.right.right = BiTreeNode(10)
        self.root.right.right.left = BiTreeNode(9)
        self.root.right.right.right = BiTreeNode(11)


def preorder_recur(root: 'BiTreeNode'):
    if root:
        print(root.data, end=' ')
        preorder_recur(root.left)
        preorder_recur(root.right)


def inorder_recur(root):
    if root:
        inorder_recur(root.left)
        print(root.data, end = ' ')
        inorder_recur(root.right)


def postorder_recur(root):
    if root:
        postorder_recur(root.left)
        postorder_recur(root.right)
        print(root.data, end = ' ')


def preorder_unrecur(root):
    
    pass








def main():
    btree = BiTree()
    btree.exampletree()
    # print('btree.root.data: ',btree.root.data)
    print('{ message: preorder_recur}')
    preorder_recur(btree.root)
    print()

    print('{ message: inorder_recur}')
    inorder_recur(btree.root)
    print()

    print('{ message: postorder_recur}')
    postorder_recur(btree.root)
    print()



if __name__ == '__main__':
    main()




# ----
