
# This script includes some sort methods wirten by me.

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

    mid = int (left + ((right-left)>>1)) # Here if don't put the cast type int (),
        # will have bug in above compare right <= left.
        # This is a # QUESTION: why?

    # print("merge_sort {0} {1} {2}".format(elements,left,mid))
    merge_sort(elements,left,mid)
    # print("merge_sort {0} {1} {2}".format(elements,mid+1,right))
    merge_sort(elements,mid+1,right)

    # print('hello')

    merge(elements,left,mid,right)

    # print(elements)
    return


def merge(elements: list, left: int, mid: int, right: int):
    if right > left:

        L = [0] * (mid-left+1)
        R = [0] * (right-mid)

        # copy the list to L[] and R[]
        j = 0
        for i in range(left,mid+1):
            L[j] = elements[i]
            j += 1

        j = 0
        for i in range(mid+1,right+1):
            R[j] = elements[i]
            j += 1

        idxleft = 0
        idxright = 0
        idxelements = left
        while idxleft < len(L) and idxright < len(R):
            if L[idxleft] <= R[idxright]:
                elements[idxelements] = L[idxleft]
                idxleft += 1
            else:
                elements[idxelements] = R[idxright]
                idxright += 1

            idxelements += 1

        while idxleft < len(L):
            elements[idxelements] = L[idxleft]
            idxleft += 1
            idxelements += 1

        while idxright < len(R):
            elements[idxelements] = R[idxright]
            idxright += 1
            idxelements += 1

        return

def quicksort(elements: list, left, right):
    if right <= left+1:
        return

    # num = elements[right-1]
    # If randomly pick the num，then it is called random quicksort
    # This can be done as follow
    import random
    randindex = random.randrange(left,right)
    num = elements[randindex]

    lidx,ridx = partion(elements,left,right,num)

    quicksort(elements,left,lidx)
    quicksort(elements,ridx,right)



def partion(elements, left, right, num):

    if right > left+1:
        small = -1
        big = right
        cur = 0

        while cur < big:
            if elements[cur] < num:
                small += 1
                elements[small], elements[cur] = elements[cur],elements[small]
                cur += 1
            elif elements[cur] > num:
                big -= 1
                elements[big], elements[cur] = elements[cur],elements[big]
            else:
                cur += 1

        lidx = small + 1
        ridx = big
        return lidx,ridx

    return left,right





























# ocupy spaces
