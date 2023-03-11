import time
from datetime import datetime

nows_time = time.time()
b_date = input("Type in your birthdate like dd mm yyyy")
your_bdate = time.mktime(time.strptime(str(b_date), '%d %m %Y'))
a = int((nows_time - your_bdate)/86400)
print(a)
