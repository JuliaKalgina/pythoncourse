import sys
import time
number = int(input("Give me a number, please"))
while number > 0:
    time.sleep(number)
    number = int(input("Give me a number, please"))
else:
    sys.exit()
