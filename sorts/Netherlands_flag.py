

def netherlands_flag(elements: list, num: int):
    length = len(elements)
    if not elements or len(elements) < 2:
        return

    small = -1
    big = length
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

    return

def main():
    import test

    for i in range(10):
        lst = test.random_array()
        print('lst: ',lst)
        if lst:
            netherlands_flag(lst,lst[0])
            print('modify lst: ',lst)



if __name__ == '__main__':
    main()


















# -----
