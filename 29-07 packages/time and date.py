from datetime import datetime,timedelta

now=datetime.now()
print(now)

future=now+timedelta(days=1)
print(future)

print(now.strftime('%d-%m-%Y  /  %H:%M minutes'))
