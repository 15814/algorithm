
# use a fixed size array to implement a stack


class stack(object):
    """docstring for stack."""


    def __init__(self, maxsize):
        super(stack, self).__init__()
        if maxsize >= 0:
            self.maxsize = maxsize
            self.st = [0] * int(maxsize)
            self._top = -1
            self._size = 0
        else:
            print('{ message: size should be larger than 0}')


    def pop(self):
        if not self.isempty():
            tmp = self.st[self._top]
            self._top -= 1
            self._size -= 1
            return tmp
        else:
            print('{ message: stack is empty! Can not do pop() }')


    def top(self):
        if self.isempty():
            return None
        return self.st[self._top]


    def isempty(self):
        if self._size <= 0:
            return True
        return False


    def push(self, elem):
        if self._size+1 > self.maxsize:
            print('{ message: the stack is full! Don\'t add the elem: }' + str(elem))
        else:
            self._size += 1
            self._top += 1
            self.st[self._top] = elem


    def size(self):
        return self._size






def main():
    st = stack(20)

    for i in range(20):
        st.push(i)

    st.push(100)
    print('st.size(): ',st.size())
    print('top: ',st.top())

    while not st.isempty():
        print(st.pop())

    st.pop()

    st.size()

    st.push(1.0)
    print(st.st[0])
    st.push("hello")
    print('st.top(): ',st.top())


if __name__ == '__main__':
    main()


# ------
