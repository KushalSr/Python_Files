import calendar

c = calendar.TextCalendar(calendar.SUNDAY)
# st = c.formatmonth(2020, 9, 0, 0)
# print(st)

# HTML formatted Calendar

# hc = calendar.HTMLCalendar(calendar.SUNDAY)
# st = hc.formatmonth(2020, 9)
# print(st)


# Days and Months


# for i in c.itermonthdays(2020, 9):
#     print(i)
#
# for name in calendar.month_name:
#     print(name)
#
# for day in calendar.day_name:
#     print(day)

# Meeting Days

print("Team meetings will be on: ")
for m in range(1, 13):
    cal = calendar.monthcalendar(202, m)
    weekone = cal[0]
    weektwo = cal[1]

    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]

    else:
        meetday = weektwo[calendar.FRIDAY]

    print("%10s %2d" %(calendar.month_name[m], meetday))
