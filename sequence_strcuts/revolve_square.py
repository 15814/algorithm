# 旋转正方形矩阵
# 【题目】 给定一个整型正方形矩阵 matrix，请把该矩阵调整成 顺时针旋转90度的样子
# 【要求】 额外空间复杂度为O(1)。


def revolve_square(matrix):
    if matrix:
        rows = len(matrix)
        cols = len(matrix[0])
        if rows != cols:
            print('{ message: matrix is not a square!!}')
            return
        if rows == 1:
            return

        lrow = 0
        lcol = 0
        rrow = rows - 1
        rcol = cols - 1

        while lrow <= rrow:
            revolve(matrix, lrow, lcol, rrow, rcol)
            lrow += 1
            lcol += 1
            rrow -= 1
            rcol -= 1


def revolve(matrix, lrow, lcol, rrow, rcol):
    print('{ message: lrow,lcol,rrow,rcol}')
    print(lrow,lcol,rrow,rcol)
    span = rcol - lcol
    if span == 0:
        return
    # if span == 1:
    #     curvalue = matrix[lrow][lcol]
    #     matrix[lrow][lcol] = matrix[rrow][lcol]
    #     matrix[rrow][lcol] = matrix[rrow][rcol]
    #     matrix[rrow][rcol] = matrix[lrow][rcol]
    #     matrix[lrow][rcol] = curvalue
    #     return

    for i in range(span):
        curvalue = matrix[lrow][lcol+i]

        matrix[lrow][lcol+i] = matrix[rcol-i][lcol]

        matrix[rcol-i][lcol] = matrix[rrow][rcol-i]

        matrix[rrow][rcol-i] = matrix[lrow+i][rcol]

        matrix[lcol+i][rcol] = curvalue

    # 相对的 index 非常重要，在这里因为忽略相对的 index，
    # 将 curvalue = matrix[lrow][lcol+i] 错写成 curvalue = matrix[lrow][i]，改了好久才发现错误。
    # 不能急，特别是 涉及到 index 的时候，很容易错，要确定好 index 之后再写，
    # 不要匆忙开始，index 没有理清，之后你就会一头雾水，不知所措！


def test(size = 10):

    for i in range(size+1):
        rows,cols = i, i
        matrix = [[0 for col in range(cols)] for row in range(rows)]

        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = cols * i + j + 1
            print('matrix[i]: ',matrix[i])

        revolve_square(matrix)
        print('{ message: after revolve}')
        for i in range(rows):
            print('matrix[i]: ',matrix[i])

        print('{ message: ----------------}\n')







def main():
    # rows, cols = 4, 4
    # matrix = [[0 for col in range(cols)] for row in range(rows)]
    #
    # for i in range(rows):
    #     for j in range(cols):
    #         matrix[i][j] = cols * i + j + 1
    #     print('matrix[i]: ',matrix[i])
    #
    # revolve(matrix,1,1,2,2)
    # print('{ message: after revolve}')
    # for i in range(rows):
    #     print('matrix[i]: ',matrix[i])

    test(10)



if __name__ == '__main__':
    main()
