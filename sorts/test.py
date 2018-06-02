

# some common functions will be used to test a method's correctness.

import sorts
from sorts import bubble_sort


def random_array(maxlength: int = 20, presicion: int = 0, maxvalue: int =100) -> list:
    """ The produced array length is in (0,100), the value of elements
        are all in (-100,100), type is float.
        If the pramater presicion set to 0, the type is int.
    """

    import random

    result = []
    length = random.randint(0,maxlength)

    if presicion > 0:
        for j in range(length):
            result.append(round(random.uniform(-1,1)*100,presicion))
    else:
        for j in range(length):
            result.append(random.randint(-maxvalue,maxvalue))

    return result


def equal_list(list1: list, list2: list) -> bool:
    """ decide whether two lists is equal ?
        If equal return true ; else return false.
        Note that if this function meet the first unequal pair, it will return and don't do the following compare operation 
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

        # a little stupid in here
        if testmethod == sorts.merge_sort:
            testmethod(copylist,0,len(copylist)-1)
            result_test = copylist[:]
        else:
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
    testmethod = sorts.merge_sort
    test_sorts(testmethod)

    # sigel testmethod
    # lst = [i for i in range(10,-1,-2)]
    # print("input: ",lst)
    # if testmethod == sorts.merge_sort:
    #     testmethod(lst,0,len(lst)-1)
    #     print(lst)
    # else:
    #     print(testmethod(lst))





    # test the equal_list() function
    # for j in range(testcases):
    #     case = random_array();
    #     equal_list(case,case)
    #
    # equal_list(case,sorted(case))




if __name__ == '__main__':
    main()
