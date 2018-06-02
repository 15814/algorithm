
class Queue(object):
    """docstring for Queue."""

    def __init__(self, maxsize=0):
        super(Queue, self).__init__()
        if maxsize >= 0:
            self._maxsize = maxsize
            self._size = 0
            self._head = -1
            self._tail = -1
            self._queue = [0] * int(maxsize)
        else:
            print('{ message: constrcut maxsize must be larger than 0}')


    def enqueue(self, elem):
        if self.full():
            print('{ message: Queue is full! enqueue {0} is fail!}.format(elem)')
        else:
            self._tail += 1
            if self._tail >= self._maxsize:
                self._tail = 0

            self._queue[self._tail] = elem

            if self.empty():
                self._head = 0

            self._size += 1



    def dequeue(self):
        if self.empty():
            print('{ message: Queue is empty. Can\'t do dequeue()}')
            return None
        else:
            elem = self._queue[self._head]
            self._head += 1
            if self._head >= self._maxsize:
                self._head = 0

            self._size -= 1
            return elem


    def empty(self):
        if self._size <= 0:
            return True
        return False


    def full(self):
        if self._size >= self._maxsize:
            return True
        return False


    def printqueue(self):
        while not self.empty():
            elem = self.dequeue()
            print(str(elem),end=' ')

        print('\n')






def main():
    queue = Queue(20)
    for i in range(20):
        queue.enqueue(i)

    for i in range(5):
        print('queue.dequeue(): ',queue.dequeue())

    # queue.printqueue()
    for i in range(3):
        queue.enqueue(i+20)

    print(queue._queue)
    print('queue._head: ',queue._head)
    print('queue._tail: ',queue._tail)

    queue.printqueue()













if __name__ == '__main__':
    main()
