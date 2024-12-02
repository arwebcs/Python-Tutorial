import datetime as d
print(d.datetime.now())
print(d.datetime(2024,5,25, 23, 45,  56))
currDate = d.datetime.now()
print(currDate.strftime("%I"))