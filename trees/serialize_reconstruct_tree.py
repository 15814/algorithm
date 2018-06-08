
import collections

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
    import binarytree

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
    print(serial_level(root))





if __name__ == '__main__':
    main()
