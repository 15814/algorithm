# 转圈打印矩阵
# 【题目】 给定一个整型矩阵matrix，请按照转圈的方式打印它。 例如:1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
# 打印结果为:1，2，3，4，8，12，16，15，14，13，9， 5，6，7，11， 10
# 【要求】 额外空间复杂度为O(1)。


def printrectangle(matrix, leftrow, leftcol, rightrow, rightcol):
    if leftrow == rightrow or leftcol == rightcol:
        if leftrow == rightrow and leftcol == rightcol:
            print(matrix[leftrow][leftcol])
        if leftrow == rightrow:
            for i in range(leftcol, rightcol+1):
                print(matrix[leftrow][i], end=' ')
        else:
            for i in range(leftrow,rightrow+1):
                print(matrix[i][leftcol], end=' ')
    else:
        for i in range(leftcol, rightcol):
            print(matrix[leftrow][i], end=' ')
        for i in range(leftrow, rightrow):
            print(matrix[i][rightcol], end=' ')
        for i in range(rightcol, leftcol, -1):
            print(matrix[rightrow][i], end=' ')
        for i in range(rightrow, leftrow, -1):
            print(matrix[i][leftcol], end=' ')


def printmatrix(matrix):
    if matrix:
        rows = len(matrix)
        cols = len(matrix[0])
        leftrow = 0
        leftcol = 0
        rightrow = rows - 1
        rightcol = cols - 1

        if rows == 1:
            for i in range(cols):
                print(matrix[0][i], end=' ')
            print()
            return

        if cols == 1:
            for i in range(rows):
                print(matrix[i][0], end=' ')
            print()
            return

        while(leftrow <= rightrow and leftcol <= rightcol):
            printrectangle(matrix, leftrow, leftcol, rightrow, rightcol)
            leftrow += 1
            leftcol += 1
            rightrow -= 1
            rightcol -= 1
            print('{ message: }')
            print(leftrow,leftcol,rightrow,rightcol)

        print('\n')
    return


def testprintmatrix():
    # case 1: empty matrix
    matrix = []
    print('{ message: case 1: empty matrix}')
    printmatrix(matrix);

    # case 2: have a empty element matrix, len = 1
    matrix =[[]]
    print('{ message: case 2: have a empty element matrix, len = 1}')
    printmatrix(matrix)

    # case 3: one row matrix
    cols, rows = 17, 1;
    matrix = [[0 for x in range(cols)] for y in range(rows)]
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = cols * i + j + 1

    print('{ message: case 3: one row matrix}')
    printmatrix(matrix)

    # case 4: one column matrix
    cols, rows = 1, 17;
    matrix = [[0 for x in range(cols)] for y in range(rows)]
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = cols * i + j + 1
    print('{ message: case 4: one column matrix}')
    printmatrix(matrix)



    # case 5: rectangle matrix
    matrix = []
    cols, rows = 5, 7;
    matrix = [[0 for x in range(cols)] for y in range(rows)]
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = cols * i + j + 1
        print('matrix[i]: ',matrix[i])
    print('{ message: rectangle matrix}')
    printmatrix(matrix)
    # print('printrectangle(matrix): ',printrectangle(matrix,0,0,5,2))

    # case 6: square matrix
    cols, rows = 8, 8;
    matrix = [[0 for x in range(cols)] for y in range(rows)]
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = cols * i + j + 1
        print('matrix[i]: ',matrix[i])
    print('{ message: square matrix}')
    printmatrix(matrix)



def main():
    # Creates a list containing 5 lists, each of 8 items, all set to 0
    cols, rows = 4, 4;
    matrix = [[0 for x in range(cols)] for y in range(rows)]

    # init the matrix to 1-16
    # for i in range(rows):
    #     for j in range(cols):
    #         matrix[i][j] = 4 * i + j + 1
    #
    # for i in range(rows):
    #     print('matrix[i]: ',matrix[i])
    #
    # printmatrix(matrix)

    testprintmatrix()



if __name__ == '__main__':
    main()






# ------
