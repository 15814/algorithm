
def q08(row, col, path_length, mark_matrix=[]):

  global global_path_count
  # print(path_count)
  if path_length <= 0:
    global_path_count += 1
    return

  if matrix[row-1][col] != 1:
    matrix[row-1][col] = 1

    q08(row-1, col, path_length-1)
    matrix[row-1][col] = 0

  if matrix[row+1][col] != 1:
    matrix[row+1][col] = 1

    q08(row+1, col, path_length-1)
    matrix[row+1][col] = 0

  if matrix[row][col-1] != 1:
    matrix[row][col-1] = 1
    q08(row, col-1, path_length-1)
    matrix[row][col-1] = 0

  if matrix[row][col+1] != 1:
    matrix[row][col+1] = 1
    q08(row,col+1, path_length-1)
    matrix[row][col+1] = 0


  # print("aaaa",path_count)
  # print(path_count)
  # return 0

def q08_2(row, col, path_length, mark_matrix=[]):
  global global_path_count

  if path_length <= 0:
    global_path_count += 1
    return

  if matrix[row+1][col] != 1:
    matrix[row+1][col] = 1
    q08(row+1, col, path_length-1)
    matrix[row+1][col] = 0

  if matrix[row][col+1] != 1:
    matrix[row][col+1] = 1
    q08(row,col+1, path_length-1)
    matrix[row][col+1] = 0


# desired result 324932
if __name__ == '__main__':
  path_length = 12
  rows = path_length + 3
  cols = path_length + 3
  global_path_count = 0
  matrix = [[0 for i in range(cols*3)] for j in range(rows*3)]
  row = rows
  col = cols
  matrix[row][col] = 1

  q08(row, col, path_length, mark_matrix=matrix)
  print(global_path_count)

  global_path_count = 0
  q08_2(row, col, path_length, mark_matrix=matrix)
  print(global_path_count,global_path_count*2)
