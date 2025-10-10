#1
import datetime
x=datetime.datetime.now()
print ((x.day-5), x.month, x.year)

#2
print ((x.day-1), x.day, (x.day+1))

#3
print (x.strftime("%x"), x.strftime("%X"))

#4
y=datetime.datetime(2007, 8, 9, 6, 0, 0)
z= (x-y)
print (z.seconds)