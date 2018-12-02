
import math

def q04(n: int, m: int):

    if m == 1:
        return n-1
    if m == 2:
        if n % 2 == 0:
            return 1+n/2
        else:
            return 1+math.floor(n/2)+1

    depth = math.log2(n)
    if m >= math.ceil(n/2):
        return depth

    # m >= 3

    firstcuts = math.ceil(math.log2(m))
    leftblocks = math.pow(2,firstcuts)
    totalcuts = firstcuts

    while leftblocks:
        




    return 0
