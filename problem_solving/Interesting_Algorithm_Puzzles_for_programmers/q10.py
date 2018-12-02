
def q10():
  eu = [0,32,15,19,4,21,2,25,17,34,6,27,13,36,11,30,8,23,10,5,24,
        16,33,1,20,14,31,9,22,18,29,7,28,12,35,3,26]
  us = [0,28,9,26,30,11,7,20,32,17,5,22,34,15,3,24,36,13,1,00,27,10,
        25,29,12,8,19,31,18,6,21,33,16,4,23,35,14,2]

  count = 0
  for n in range(2,36+1):
    if max_n(eu,n) < max_n(us,n):
      count += 1

  print('count: ',count)
  return count

def max_n(lst, n):
  if n > len(lst):
    return None

  max = 0
  for i in range(n):
    max += lst[i]

  cur_total = max

  left_idx = 0
  right_idx = n
  for i in range(n,2*len(lst)):

    if right_idx >= len(lst):
      right_idx = 0
    if left_idx >= len(lst):
      break

    cur_total += lst[right_idx]-lst[left_idx]
    left_idx += 1
    right_idx += 1
    if cur_total > max:
      max = cur_total

  return max



if __name__ == '__main__':
  q10()
