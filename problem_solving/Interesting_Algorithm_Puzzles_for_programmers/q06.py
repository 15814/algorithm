

def q06(max):
  count = 0
  if max < 2:
    return count

  for i in range(2,max,2):
    n = 3 * i + 1
    while n != 1 and n != i:
      if n % 2 == 0:
        n = n/2
      else:
        n = 3 * n + 1

    if n == i:
      count += 1

  print(count)
  return count

if __name__ == '__main__':
  max = 10000
  q06(max)
