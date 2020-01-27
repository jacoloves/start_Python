import time
fmt = "It's %A, %B %d, %Y, local time %I:%M:%S%p"
t = time.localtime()
print(t)

print(time.strftime(fmt, t))

from datetime import date
some_day = date(2014, 7, 4)
print(some_day.strftime(fmt))

from datetime import time
some_time = time(10, 35)
print(some_time.strftime(fmt))
