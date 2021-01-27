import datetime

my_time = datetime.time(23,59,59,132)
print(my_time)
print(my_time.hour)
print(my_time.minute)
print(my_time.second)
print(my_time.microsecond)
my_date = datetime.date.today()
print(my_date)
print(my_date.year)
print(my_date.month)
print(my_date.day)
print(my_date.ctime())
from datetime import datetime

mydatetime = datetime(2021,10,3,14,20)
print(mydatetime)
mydatetime = mydatetime.replace(year = 2023)
print(mydatetime)

from datetime import date

date1 = date(2021, 11, 3)
date2 = date(2020, 11, 3)
result = date1 - date2
print(result.days)
