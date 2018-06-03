def printrectangle(matrix, leftrow, leftcol, rightrow, rightcol):
    if leftrow <= rightrow:
        for i in range(leftcol, rightcol):
            print(matrix[leftrow][i], end=' ')
        for i in range(leftrow, rightrow):
            print(matrix[i][rightcol], end=' ')
        for i in range(rightcol, leftcol, -1):
            print(matrix[rightcol][i], end=' ')
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

        while(leftrow <= rightrow):
            printrectangle(matrix, leftrow, leftcol, rightrow, rightcol)
            leftrow += 1
            leftcol += 1
            rightrow -= 1
            rightcol -= 1

        print('\n')
    return

