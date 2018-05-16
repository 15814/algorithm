
import sorts
from sorts import bubble_sort


def random_array(maxlength: int = 20, presicion: int = 4) -> list:
    """ The produced array length is in (0,100), the value of elements
        are all in (-100,100), type is float.
    """

    import random

    result = []
    length = random.randint(0,maxlength)

    for j in range(length):
        result.append(round(random.uniform(-1,1)*100,presicion))

    return result


def equal_list(list1: list, list2: list) -> bool:
    """ decide whether two lists is equal ?
        If equal return true ; else return false.
     """

    if len(list1) != len(list2):
        return False
    work = 1
    for (i,v) in enumerate(list1):
        if v != list2[i]:
            print("The difference starts in {0} vs {1}".format((i,v),(i,list2[i])))
            print(list1)
            print(list2)
            work = 0
            break

    if work:
        return True
    else:
        return False

def test_sorts(testmethod: 'function' = bubble_sort,testcases: 'int' =3000) -> bool:
    work = 1
    for i in range(testcases):
        testlist = random_array()
        copylist = testlist[:]
        result_test = testmethod(copylist)
        result_true = sorted(testlist)
        if not equal_list(result_test,result_true):
            work = 0
            print("orginal: %s" % testlist)
            print("test: %s" % result_test)
            print("true: %s" % result_true)
            break
    if work:
        print(str(testmethod) + 'is OK!')
        print(testlist)
        print(result_test)
        print(result_true)
        return True
    else:
        return False




def main():
    testcases = 3000
    testmethod = sorts.bubble_sort
    test_sorts(testmethod)

    lst = [-79, 46, -47, 34, -92, -66, 16, -87, -88, -22]
    print(lst)
    print(testmethod(lst))




    # test the equal_list() function
    # for j in range(testcases):
    #     case = random_array();
    #     equal_list(case,case)
    #
    # equal_list(case,sorted(case))




if __name__ == '__main__':
    main()
