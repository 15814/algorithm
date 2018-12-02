
def q03():
    lst = [ False for i in range(1,101)]
    # print(lst)
    mark = True
    n = 2
    while mark:
        mark = False
        for index in range(n-1,100,n):
            lst[index] = (not lst[index])
            mark = True
        n += 1

    for i in range(len(lst)):
        if not lst[i]:
            print(i+1,end=',')
    print()

def q03_2():
    lst = [False for i in range(0,101)]

    for index in range(2,101):
        for gap in range(2,101):
            if index % gap == 0:
                lst[index] = (not lst[index])

    for i in range(1,101):
        if not lst[i]:
            print(i,end=',')
    print()

q03()
q03_2()
