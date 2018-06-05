
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


    def reverse(self):
        # empty or one node
        if self.head == None or self.head.next == None:
            return

        # two nodes
        if self.head.next.next == None:
            cur = self.head.next
            cur.next = self.head

            self.head.next = None

            self.head = cur
            return


        cur1 = self.head
        cur2 = cur1.next
        keep = cur2.next

        while keep != None:
            cur2.next = cur1

            cur1 = cur2
            cur2 = keep
            keep = keep.next

        cur2.next = cur1

        self.head.next = None

        self.head = cur2


def test(size=10):
    for i in range(size+1):
        llst = LinkedList()
        for j in range(i):
            llst.add(j)

        llst.printlist()
        llst.reverse()
        llst.printlist()
        print('\n')


def main():
    test(20)




if __name__ == '__main__':
    main()



# ----------
