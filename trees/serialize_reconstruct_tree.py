

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


def deserialpre(string):
    root = Node()
    if not string or string[0] == '#':
        return root
    else:
        lst = preprocess(string)


def reconstrcutbypre(lst, begin, curnode):

    if lst[begin+1] != '#':
        left = Node(lst[begin+1])
        curnode.left = left
        begin += 1
        curnode = left
        reconstrcutbypre(lst, begin, curnode)
    else:
        curnode.left = None





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
    root = getexampletree()
    print(serialbypre(root))








if __name__ == '__main__':
    main()
