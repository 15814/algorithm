
def bubble_sort(elements: list) -> list:
    length = len(elements)

    for i in range(len(elements)):
        work = 0
        for i in range(length-1):
            if elements[i] > elements[i+1]:
                elements[i], elements[i+1] = elements[i+1], elements[i]
                work = 1

        if work == 0:
            break
    return elements


def selection_sort(elements: list) -> list:
    length = len(elements)

    for i in range(length):
        begin = i
        end = length
        min = elements[i]
        min_idx = i
        for j in range(begin+1,end):
            if elements[j] < min:
                min = elements[j]
                min_idx = j
        elements[begin],elements[min_idx] = elements[min_idx], elements[begin]

    return elements

def insertion_sort(elements: list):
    length = len(elements)
    for i in range(1,length):
        cur = i
        while cur >= 1 and elements[cur] < elements[cur-1]:
            elements[cur-1], elements[cur] = elements[cur], elements[cur-1]
            cur -= 1   # don't use --cur in python


    return elements


def merge_sort(elements: list, left: int, right: int):
    if right <= left:
        return

    mid = int (left + ((right-left)>>1))

    # print("merge_sort {0} {1} {2}".format(elements,left,mid))
    merge_sort(elements,left,mid)
    # print("merge_sort {0} {1} {2}".format(elements,mid+1,right))
    merge_sort(elements,mid+1,right)

    # print('hello')
    tmplist = []
    idxleft = left
    idxright = right
    while idxleft <= mid and idxright <= right:
        if elements[idxleft] <= elements[idxright]:
            tmplist.append(elements[idxleft])
            idxleft += 1
        else:
            tmplist.append(elements[idxright])
            idxright += 1

    print("no tail",tmplist)
    
    if(idxleft > mid):
        for i in range(idxright,right+1):
            tmplist.append(elements[i])
    else:
        for i in range(idxleft,mid+1):
            tmplist.append(elements[i])


    print(tmplist)
    return












# ocupy spaces
