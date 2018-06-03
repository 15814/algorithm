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
