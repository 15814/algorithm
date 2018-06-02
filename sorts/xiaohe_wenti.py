
def truemethod(elements: list):
    sum = 0
    for i in range(len(elements)):
        j = 0
        while j < i:
            if elements[j] < elements[i]:
                sum += elements[j]
            j += 1

    return sum

def smallsum(elements: list):
    if not elements or len(elements) < 2:
        return 0
    return merge_sort(elements,0,len(elements))

def merge_sort(elements: list, left: int, right: int):
    """ elements includes elements[left] but don't includes elements[right] """

    # sum = 0
    if right-left > 1:
        mid = int (left + ((right-left)>>1))
        return merge_sort(elements,left,mid) \
               + merge_sort(elements,mid,right) \
               + merge(elements,left,mid,right)

    return 0


def merge(elements: list, left: int, mid: int, right: int):

    leftlist = [0]*(mid-left)
    rightlist = [0]*(right-mid)

    j = 0
    for i in range(left,mid):
        leftlist[j] = elements[i]
        j += 1

    j = 0
    for i in range(mid,right):
        rightlist[j] = elements[i]
        j += 1

    idxleft = 0
    idxright = 0
    idxelements = left
    sum = 0
    while idxleft < len(leftlist) and idxright < len(rightlist):
        if leftlist[idxleft] < rightlist[idxright]:
            elements[idxelements] = leftlist[idxleft]
            sum += leftlist[idxleft] * (len(rightlist)-idxright)
            idxleft += 1
        else:
            elements[idxelements] = rightlist[idxright]
            idxright += 1

        idxelements += 1

    while idxleft < len(leftlist):
        elements[idxelements] = leftlist[idxleft]
        # sum += leftlist[idxleft] * (len(leftlist)-idxleft-1)
        idxleft += 1
        idxelements += 1

    while idxright < len(rightlist):
        elements[idxelements] = rightlist[idxright]
        # sum += rightlist[idxright] * (len(rightlist)-idxright-1)
        idxright += 1
        idxelements += 1

    # print(left,mid,right,sum)
    # print(elements)
    return sum


def main():
    lst = [1,3,4,2,5]
    print("true sum is: ",truemethod(lst))
    print("sum is:",smallsum(lst))
    print(lst)

    # for test
    import test
    testcases = 1000
    for i in range(testcases):
        randlist = test.random_array(100,0,100)
        copylist = randlist[:]
        copylist2 = randlist[:]
        result_test = smallsum(copylist)
        result_true = truemethod(copylist2)

        if result_true != result_test:
            print('{message: }something wrong')
            print("orignal list: ",randlist)
            print("test result: ", result_test)
            print("true result: ", result_true)
            break;

    # print('randlist',randlist)
    # print('result_test: ',result_test)




if __name__ == '__main__':
    main()
