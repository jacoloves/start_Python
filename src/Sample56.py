import datetime

date = datetime.datetime(year=2018, month=5, day=25, hour=12, minute=0, second=0)
message = '{0.year}年{0.month}月{0.day}日'.format(date)
print(message)