#

class Node(object):
    """docstring for Node."""

    def __init__(self, data = None):
        super(Node, self).__init__()
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None


    def add(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node


    def printlist(self):
        cur = self.head

        while cur != None:
            print(cur.data, end=' ')
            cur = cur.next

        print('\n')
