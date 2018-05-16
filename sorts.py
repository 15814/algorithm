
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
