

import collections


class BiTreeNode(object):
    """docstring for Node."""

    def __init__(self, data = None, left = None, right = None):
        super(BiTreeNode, self).__init__()
        self.data = data
        self.left = left
        self.right = right


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
    st = collections.deque()
    if root:
        st.append(root)
        while st:
            popnode = st.pop()
            print(popnode.data, end = ' ')

            if popnode.right:
                st.append(popnode.right)
            if popnode.left:
                st.append(popnode.left)
    print()


def inoreder_unrecur(root):
    st = collections.deque()
    s = set()

    if root:
        st.append(root)

        while st:
            popnode = st.pop()
            if popnode not in s:
                if popnode.right:
                    st.append(popnode.right)
                s.add(popnode)
                st.append(popnode)
                if popnode.left:
                    st.append(popnode.left)
            else:
                print(popnode.data, end = ' ')
    print()


def inoreder_unrecur2(root):
    st = collections.deque()
    if root:
        head = root
        while st or head:
            if head:
                st.append(head)
                head = head.left
            else:
                popnode = st.pop()
                print(popnode.data, end=' ')
                head = popnode.right

    print()



def postorder_unrecur(root):

    st = collections.deque()
    s = set()
    if root:
        st.append(root)
        while st:
            popnode = st.pop()
            if popnode not in s:
                st.append(popnode)
                s.add(popnode)
                if popnode.right:
                    st.append(popnode.right)
                if popnode.left:
                    st.append(popnode.left)
            else:
                print(popnode.data, end = ' ')
    print()


def postorder_unrecur2(root):

    st = collections.deque()
    st2 = collections.deque()
    if root:
        st.append(root)
        while st:
            popnode = st.pop()
            # print(popnode.data, end = ' ')
            st2.append(popnode.data)
            if popnode.left:
                st.append(popnode.left)
            if popnode.right:
                st.append(popnode.right)

        while st2:
            print(st2.pop(), end = ' ')
        print()


def postorder_unrecur3(root):
    # request: Auxiliary space complexity is O(1)
    st = collections.deque()

    if root:
        st.append(root)
        pre = root
        while st:
            head = st.pop()
            if (not head.left and not head.right) or head.left == pre or head.right == pre:
                print(head.data, end = ' ')

            else:
                st.append(head)
                if head.right:
                    st.append(head.right)
                if head.left:
                    st.append(head.left)
            pre = head



def main():
    btree = BiTree()
    btree.exampletree()
    root = btree.root
    # print('btree.root.data: ',btree.root.data)
    print('{ message: preorder_recur}')
    preorder_recur(root)
    print()

    print('{ message: inorder_recur}')
    inorder_recur(root)
    print()

    print('{ message: postorder_recur}')
    postorder_recur(root)
    print('---------\n')

    print('{ message: preorder_unrecur}')
    preorder_unrecur(root)

    print('{ message: inoreder_unrecur}')
    inoreder_unrecur(root)

    print('{ message: postorder_unrecur}')
    postorder_unrecur(root)

    print('inoreder_unrecur2(): ')
    inoreder_unrecur2(root)

    print('{ message: postorder_unrecur2}')
    postorder_unrecur2(root)

    print('{ message: postorder_unrecur3}')
    postorder_unrecur3(root)


if __name__ == '__main__':
    main()




# ----
