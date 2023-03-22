import datetime

date = datetime.datetime.now()
year = str(date.year)
month = str(date.month) if len(str(date.month)) == 2 else "0" + str(date.month)
day = str(date.day) if len(str(date.day)) == 2 else "0" + str(date.day)
print(year + "-" + month + "-" + day)