# Calendat Module

"""

"""

import calendar

n1,n2,n3=map(int,input().split())
print((calendar.day_name[calendar.weekday(n3,n1,n2)]).upper())


# print(calendar.TextCalendar(firstweekday=6).formatyear(2015))