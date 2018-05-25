
# This script usage : big heap (max value in heap's top)


def heapinsert(elements: list, elem):
    if not elements:
        elements.append(elem)
        return

    elements.append(elem)
    length = len(elements)
    addidx = length - 1
    parent = int ((addidx-1)/2)
    while addidx > 0 and elements[addidx] > elements[parent]:
        elements[addidx], elements[parent] = elements[parent],elements[addidx]
        addidx = parent
        parent = int ((addidx-1)/2)

    return


def printheap(elements: list):
    # printheap() 在命令行下的打印受限于每行最大80字符，
    # 不应该去模仿打印理想的树图，
    # 应该像是GitHub打印它的branch图那样才有可能在节点数很多的时候依然具备可读性
    # 这里的 printheap 只在节点数小于20时有不错的效果，需要改进

    import math

    length = len(elements)
    layors = math.ceil(math.log2(length+1))
    lastlayornodes = 2**(layors-1)
    maxwidth =  lastlayornodes + (lastlayornodes-1) * 4
    # prespaces = int (maxwidth/2)
    for i in range(layors):
        spacescount = int (maxwidth / (i+1))
        spaces = ' ' * spacescount
        halfspaces = ' ' * int (spacescount/2)
        space4 = ' ' * 4
        count = 1
        for j in range(2**i-1,2**(i+1)-1):
            if j < length:
                if i > 1 and count > 1 and count % 2 != 0:
                        print(halfspaces + str(elements[j]),end = '')
                else:
                    print(spaces + str(elements[j]),end = '')
                count += 1
        print('\n')

    return


def heap_pop(elements: list):
    if not elements:
        return

    elements[0],elements[len(elements)-1] = elements[len(elements)-1],elements[0]

    elem = elements.pop(len(elements)-1)
    if elements:
        heapify(elements)

    return elem


def heapify(elems: list):
    if not elems or len(elems) == 1:
        return
    if len(elems) == 2:
        if elems[0] < elems[1]:
            elems[0], elems[1] = elems[1], elems[0]

    if len(elems) > 2:
        cur = 0
        lchild = 2 * cur + 1
        rchild = lchild + 1
        while elems[cur] < elems[lchild] or elems[cur] < elems[rchild]:
            max = (lchild if elems[lchild] > elems[rchild] else rchild)
            elems[cur], elems[max] = elems[max], elems[cur]
            cur = max
            lchild = 2 * cur + 1
            rchild = lchild + 1
            if lchild >= len(elems):
                break
            if rchild >= len(elems):
                rchild = lchild

        return





def test_heapinsert(elems: list, testcases: int = 10):
    import random
    for i in range(testcases):
        elem = random.randrange(1,100)
        heapinsert(elems,elem)
    printheap(elems)

def test_heap_pop(elems: list):
    fourspaces = '    '
    while elems:
        print(heap_pop(elems),end=fourspaces)

    return

def heap_sort(elems: list):

    pass


def main():
    elems =[]
    test_heapinsert(elems,20)
    test_heap_pop(elems)

if __name__ == '__main__':
    main()


# --- occupy spaces
