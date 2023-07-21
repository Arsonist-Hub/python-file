from datetime import date

t=date.today()

print ("today date",t)
print ("current year",t.year)
print ("scurrent month",t.month)
print ('current day',t.day)

import time

print (time.time())
print (time.ctime())

for i in range(20):
    print(i)
    time.sleep(2)
    