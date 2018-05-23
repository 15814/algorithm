
# use for run some tests on methods


def foo(arg1: int =1):
    if hasattr(int,'arg1'):
        print('hasattr')
    else:
        print('not hasattr')
        print(arg1)


def main():
    # foo()
    # print(type(foo))

    test_quicksort()




def test_quicksort(cases: int = 20):
    import test
    import sorts
    for i in range(cases):
        lst = test.random_array()
        # print('lst: ',lst)
        lstcopy = lst[:]
        sorts.quicksort(lstcopy,0,len(lstcopy))
        print('sorted lst: ',lstcopy)
        test.equal_list(lstcopy,sorted(lst))

    print('{ message: no other things means everything is ok! }')

    lst = [2,1,2,2,2,2,2,2,2]
    sorts.quicksort(lst,0,len(lst))
    print('lst: ',lst)






















if __name__ == '__main__':
    main()
