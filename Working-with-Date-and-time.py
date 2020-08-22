from datetime import date
from datetime import time
from datetime import datetime


# Code for Date

today = date.today()

print("Today's date is ", today)
print("Date components: ", "Day = ", today.day, ", Month = ",
      today.month, ", Year = ", today.year)

print("Today's weekday # is : ", today.weekday())

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print("Which is a ", days[today.weekday()])

# Code for time

today = datetime.now()
print("The current date and time is ", today)

t = datetime.time(datetime.now())
print(t)




