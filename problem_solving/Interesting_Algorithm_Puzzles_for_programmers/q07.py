import pandas as pd
from datetime import datetime


def getdatelist(begindate, enddate):
    # beginDate, endDate是形如‘20160601’的字符串或datetime格式
    date_lst = [datetime.strftime(x,'%Y%m%d') for x in list(pd.date_range(start=begindate, end=enddate))]
    return date_lst


def q07(begindate='19641010',enddate='20200724'):
  date_lst = [int(x) for x in getdatelist(begindate,enddate)]

  for date in date_lst:
    numstr = format(date,'b')
    numstr_reverse = numstr[::-1]
    if numstr == numstr_reverse:
      print(date)
    # print(numstr,numstr_reverse)

# 即使采用同一种方法，只要稍微花点工夫优化，处理时间就能大幅度缩短。编程的时候务必要兼顾程序的可读性、处理效率及可扩展性

if __name__ == '__main__':
  q07()
