from datetime import datetime,timedelta

today=datetime.today().date()
tomorrow=today + timedelta(days=1)
yesterday=today - timedelta(days=1)
print(today,tomorrow,yesterday)

p=datetime.now()
l= p+timedelta(hours=6,milliseconds=67676767676767)

print (p,l)

d1=datetime(2025,12,25)
d2=datetime(91,8,8)
print(d1-d2)
