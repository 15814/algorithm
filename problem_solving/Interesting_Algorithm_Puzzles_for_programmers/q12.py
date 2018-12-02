
import math
import decimal
from decimal import Decimal

def q12():
  decimal.getcontext().prec = 20
  # print(decimal.Decimal.sqrt(Decimal(2)))
  min = 1000
  min_num = -1
  min2 = 1000
  min_num2 = -1
  dd = 10e5

  for num in range(2,int(dd)):
    r = decimal.Decimal.sqrt(Decimal(num))
    if not float(r).is_integer():
      count = 0
      num_str = str(r)
      check_set = set([str(i) for i in range(0,9+1)])
      for num_ch in num_str:
        if min == 10:
          break
        if not check_set:
          break
        if num_ch != '.':
          check_set.discard(num_ch)
          count += 1
      if count != 0 and count < min:
        min = count
        min_num = num

      decimal_str = num_str.split('.')[-1]
      check_set2 = set([str(i) for i in range(0,9+1)])
      count2 = 0
      for num_ch in decimal_str:
        if min2 == 10:
          break
        if not check_set2:
          break
        check_set2.discard(num_ch)
        count2 += 1
      if count2 != 0 and count2 < min2:
        min2 = count2
        min_num2 = num
      if min == 10 and min2 == 10:
        break


  print('min: ',min)
  print('min_num: ',min_num,decimal.Decimal.sqrt(Decimal(min_num)))

  print('min2',min2)
  print('min_num2: ',min_num2)
  print(': ', decimal.Decimal.sqrt(Decimal(min_num2)))




if __name__ == '__main__':
  q12()
