# https://pynative.com/python-datetime-format-strftime/

from datetime import datetime


now = datetime.now()

dt_time_str = now.strftime("%Y-%m-%d %H:%M:%S")

print("Date Time String",dt_time_str)

print("Time String",now.strftime("%H:%M:%S"))
print("Date String - 1:",now.strftime("%d/%m%/%Y"))
print("Date String - 2:",now.strftime("%d/%m%/%y"))
print("Date String - 3:",now.strftime("%d/%m%/%y,%A"))
print("Date String - 4:",now.strftime("%d %b% %Y,%a"))
print("Date String - 5:",now.strftime("%d %B% %Y,%a"))


