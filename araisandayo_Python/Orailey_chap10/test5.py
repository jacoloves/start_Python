from datetime import date, timedelta
birthday = date(1993, 1, 16)
print(birthday)

print(birthday.weekday())
print(birthday.isoweekday())

sample = birthday + timedelta(days=10000)
print(sample)