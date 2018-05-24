
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



def test_heap():
    import random
    elements = []
    for i in range(10):
        elem = random.randrange(1,100)
        heapinsert(elements,elem)
    printheap(elements)





def main():
    test_heap()


if __name__ == '__main__':
    main()


# --- occupy spaces
