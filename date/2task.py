import datetime
print("Yesterday was: ", datetime.date.today() - datetime.timedelta(days=1), "\nToday is: ", datetime.date.today(), "\nTomorrow will be: ", datetime.date.today() + datetime.timedelta(days=1))
