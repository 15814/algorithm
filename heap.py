
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
    import math

    length = len(elements)
    layors = math.ceil(math.log2(length+1))
    lastlayornodes = 2**(layors-1)
    maxwidth =  lastlayornodes + (lastlayornodes-1) * 4

    for i in range(layors):
        spacescount = int (maxwidth / (i+1))
        spaces = ' '* spacescount
        for j in range(2**i-1,2**(i+1)-1):
            if j < length:
                print(spaces + str(elements[j]),end = '')
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





def test_heapinsert(elems: list):
    import random
    for i in range(10):
        elem = random.randrange(1,100)
        heapinsert(elems,elem)
    printheap(elems)

def test_heap_pop(elems: list):
    while elems:
        print(heap_pop(elems),end='    ')

    return




def main():
    elems =[]
    test_heapinsert(elems)
    test_heap_pop(elems)

if __name__ == '__main__':
    main()


# --- occupy spaces
