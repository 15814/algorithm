
import math

def q11():
  a1 = 1
  a2 = 1

  result = []
  result2 = []

  while len(result) < 15:
    b = a1 + a2
    a1 = a2
    a2 = b
    if b % get_pos_sum(b) == 0:
      result.append(b)
    if b % get_pos_sum2(b) == 0:
      result2.append(b)
  print(result)
  print(result2)
  print("2^31-1",1<<32 - 1)
  # print(math.pow(2,32))
  return

def get_pos_sum(num:int):
  pos = []
  pos.append(num%10)
  num = math.floor(num/10)
  while num:
    pos.append(num%10)
    num = math.floor(num/10)

  sum = 0
  for elem in pos:
    sum += elem

  return sum

def get_pos_sum2(num):
  pos = []
  string = str(num)
  sum = 0
  for ch in string:
    sum += int(ch)
  return sum


if __name__ == '__main__':
  q11()
