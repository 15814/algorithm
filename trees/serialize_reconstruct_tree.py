
import collections
import binarytree

class Node(object):
    """docstring for Node."""
    def __init__(self, data = None, left = None, right = None, parent = None):
        super(Node, self).__init__()
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent


def serialbypre(root):
    """ serial a tree by travel preorder, return a string. """

    result = ''
    if root:
        result += str(root.data) + '_' + serialbypre(root.left) \
                  + serialbypre(root.right)
    else:
        result += '#_'

    return result

# 思路混乱时，没有想清楚就开始写代码时的遗物
# def deserialpre(string):
#     root = Node()
#     if not string or string[0] == '#':
#         return root
#     else:
#         lst = preprocess(string)


# def reconstrcutbypre(lst, begin, curnode):
#
#     if lst[begin+1] != '#':
#         left = Node(lst[begin+1])
#         curnode.left = left
#         begin += 1
#         curnode = left
#         reconstrcutbypre(lst, begin, curnode)
#     else:
#         curnode.left = None
# ------------


def deserialprestring(string):
    root = Node()
    if not string or string[0] == '#':
        return root
    else:
        lst = string.split('_')
        deque = collections.deque()
        for data in lst:
            node = Node(data)
            deque.append(node)

        return deserialpre(deque,root)


def deserialpre(deque, root):
    root = deque.popleft()
    if root.data == '#':
        return None
    root.left = deserialpre(deque,root.left)
    root.right = deserialpre(deque,root.right)
    return root


def serial_level(root):
    queue = collections.deque()
    string =''
    if root:
        queue.append(root)
        while queue:
            node = queue.popleft()
            string += str(node.data) + '_'
            if node.data != '#':
                if node.left:
                    queue.append(node.left)
                else:
                    queue.append(Node('#'))
                if node.right:
                    queue.append(node.right)
                else:
                    queue.append(Node('#'))
    else:
        string += '#'
    return string


def deserial_levelstring(string):
    root = Node()
    if not string or string[0] == '#':
        return root
    else:
        lst = string.split('_')
        deque = collections.deque(lst)
        return deserial_level(deque, root)


def deserial_level(deque, root):
    if deque:
        root = Node(deque.popleft())
        node = root
        parents = collections.deque()
        parents.append(root)

        while deque and parents:
            parent = parents.popleft()
            leftdata = deque.popleft()
            if leftdata != '#':
                left = Node(leftdata)
                parent.left = left
                parents.append(left)
            else:
                parent.left = None

            if not deque:
                return root

            rightdata = deque.popleft()
            if rightdata != '#':
                right = Node(rightdata)
                parent.right = right
                parents.append(right)
            else:
                parent.right = None

    return root


def preprocess(string):
    lst =[]
    begin = 0
    while begin < len(string):
        if string[begin] == '#':
            lst.append('#')
            begin = begin + 2
        else:
            end = begin + 1
            while end < len(string) and string[end] != '_':
                end += 1
            data = int (string[begin:end])
            lst.append(data)
            begin = end + 1

    return lst


def serialbyin(root):
    string = ''
    if root:
        if not root.left and not root.right:
             string += '#_' + str(root.data) + '_' + '#_'

        if root.left and not root.right:
            string += serialbyin(root.left) + str(root.data) + '_' + '#_'

        if root.right and not root.left:
            string += '#_' + str(root.data) + '_' + serialbyin(root.right)

        if root.left and root.right:
            string += serialbyin(root.left) + str(root.data) + '_' + serialbyin(root.right)

        return string


def serialbyin2(root):
    if root:
        return serialbyin2(root.left) + str(root.data) + '_'  \
               + serialbyin2(root.right)

    else:
        return '#_'


def deserialinstring(string):
    root = Node()
    if string and string[1] != '#':
        lst = string.split('_')
        deque = collections.deque(lst)
        deserialin(deque, root)
        return root
    else:
        return root


def deserialin(deque, root):
    leftdata = deque.popleft()
    # 　而仅根据（带空指针的）中序遍历，是不能重建二叉树的。比如，上面这棵树的中序遍历为 #2#1#3#4#。事实上可以证明，任何一棵二叉树的中序遍历结果，都会是空指针与树中结点交替出现的形式，所以空指针没有提供任何额外的信息。
    # 具体见 https://blog.csdn.net/gettogetto/article/details/70244827 好文章，关于二叉树序列化和重建的各种事情都讲得非常清楚、全面！




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


def test():
    head = Node()


    pre = serialbypre(head)
    print("serialize tree by pre-order: " + pre)
    head = deserialprestring(pre)
    print("reconstruct tree by pre-order, ")
    binarytree.levelorder(head)

    level = serial_level(head)
    print("serialize tree by level: " + level)
    head = deserial_levelstring(level)
    print("reconstruct tree by level, ")
    binarytree.levelorder(head)

    print("====================================")

    head = Node(1)


    pre = serialbypre(head)
    print("serialize tree by pre-order: " + pre)
    head = deserialprestring(pre)
    print("reconstruct tree by pre-order, ")
    binarytree.levelorder(head)

    level = serial_level(head)
    print("serialize tree by level: " + level)
    head = deserial_levelstring(level)
    print("reconstruct tree by level, ")
    binarytree.levelorder(head)

    print("====================================")

    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    head.right.right = Node(5)


    pre = serialbypre(head)
    print("serialize tree by pre-order: " + pre)
    head = deserialprestring(pre)
    print("reconstruct tree by pre-order, ")
    binarytree.levelorder(head)

    level = serial_level(head)
    print("serialize tree by level: " + level)
    head = deserial_levelstring(level)
    print("reconstruct tree by level, ")
    binarytree.levelorder(head)

    print("====================================")

    head = Node(100)
    head.left = Node(21)
    head.left.left = Node(37)
    head.right = Node(-42)
    head.right.left = Node(0)
    head.right.right = Node(666)


    pre = serialbypre(head)
    print("serialize tree by pre-order: " + pre)
    head = deserialprestring(pre)
    print("reconstruct tree by pre-order, ")
    binarytree.levelorder(head)

    level = serial_level(head)
    print("serialize tree by level: " + level)
    head = deserial_levelstring(level)
    print("reconstruct tree by level, ")
    binarytree.levelorder(head)

    print("====================================")





def main():


    root = getexampletree()
    print('{ message: preorder_unrecur}')
    binarytree.preorder_unrecur(root)

    serialstring = serialbypre(root)
    print(serialstring)


    reconroot = deserialprestring(serialstring)
    print('{ message: }')
    binarytree.preorder_unrecur(reconroot)

    print('{ message: level travel}')
    binarytree.levelorder(root)
    print('{ message: serial_level}')
    serial_levelstr = serial_level(root)
    print(serial_levelstr)

    print('{ message: deserial_level}')
    node = deserial_levelstring(serial_levelstr)
    binarytree.levelorder(node)

    print('{ message: serialbyin}')
    print(serialbyin(root))

    print('{ message: serialbyin2}')
    print(serialbyin2(root))

    print('====================\n')


    # test()


if __name__ == '__main__':
    main()
