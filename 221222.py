import datetime as dt

x=dt.datetime.now()
#x.hour("%H")
x.strftime("%A %d. %B %Y")
print(x)