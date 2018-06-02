
# 问题二(荷兰国旗问题)
# 给定一个数组arr，和一个数num，请把小于num的数放在数组的 左边，等于num的数放在数组的中间，大于num的数放在数组的 右边。
# 要求额外空间复杂度O(1)，时间复杂度O(N)

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
