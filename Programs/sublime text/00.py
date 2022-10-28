
import calendar
import datetime
import time

print(calendar.weekheader(3))
print()

print(calendar.firstweekday())
print()

print(calendar.month(2020, 9))

print(calendar.calendar(2020))

day_of_the_week = calendar.weekday(2020, 9, 21)
print(day_of_the_week)

is_leap = calendar.isleap(2020)
print(is_leap)

how_many_leap_day = calendar.leapdays(2000,2020)
print(how_many_leap_day)