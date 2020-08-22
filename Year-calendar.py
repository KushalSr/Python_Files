import calendar

c = calendar.TextCalendar(calendar.SUNDAY)

year = c.formatyear(2020, 1, 0, 1)

print(year)