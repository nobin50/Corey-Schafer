import datetime
import pytz

t = datetime.date(2018, 7, 17)
print(t)

tday = datetime.date.today()
print(tday)
print(tday.year)
print(tday.month)
print(tday.weekday())  # Monday starts with 0 & sunday 6
print(tday.isoweekday())  # Monday starts with 1 & sunday 7

tdelta = datetime.timedelta(days=7)
print(tday - tdelta)
print(tday + tdelta)

bday = datetime.date(2019, 3, 16)
till_day = bday - tday
print(till_day)
print(till_day.days)
print(till_day.total_seconds())

tm = datetime.time(10, 41, 23)
print(tm)
print(tm.hour)

dttm = datetime.datetime(2018, 7, 17, 10, 43, 25)
print(dttm)
print(dttm.time())
print(dttm.minute)

tmdelta = datetime.timedelta(days=8)
print(dttm + tmdelta)

tmdelta1 = datetime.timedelta(hours=14)
print(dttm + tmdelta1)


print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)


'''
for tz in pytz.all_timezones:
    print(tz)
'''

dt_mtn = dt_utcnow.astimezone((pytz.timezone('Asia/Dhaka')))
print(dt_mtn)

print(dt_mtn.isoformat())

print(dt_mtn.strftime('%B %d, %Y'))

