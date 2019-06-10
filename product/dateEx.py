from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
from datetime import tzinfo


today = date.today()
# print(today)
# print("{}-{}-{}".format(today.day, today.month, today.year))
# print(today.weekday())

givndt = datetime(2019, 5, 22, 23, 59, 59, 999999) #.strftime("%Y, %m, %d, %H, %M, %S
print givndt.strftime("%Y-%m-%d")

curDay = givndt.weekday()
stardDay = 0
lstDay = 6 - curDay

fDay = givndt - timedelta(days=curDay)
lDay = givndt + timedelta(days=lstDay)
print fDay
print lDay


print givndt.weekday()

# print datetime.now().weekday()
# print datetime.now() - timedelta(days=6)
