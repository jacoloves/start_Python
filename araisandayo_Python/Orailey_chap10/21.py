from datetime import date
now = date.today()
print(now)

from datetime import timedelta
one_day = timedelta(days=1)
tomorrow = now + one_day
print(tomorrow)

print(now + 17*one_day)

yesterday = now - one_day
print(yesterday)