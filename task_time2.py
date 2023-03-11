import time
from datetime import datetime
counting = time.time()
your_number = int(input('Type in a random positive number'))
time.sleep(3)
your_number2 = int(input('Type in another positive number'))
if your_number > 0:
    new_n = your_number * your_number2
    print(new_n, "That's your two numbers multiplied")
time_taken = time.time() - counting
name = 'times_{}.txt'.format(datetime.now().strftime('%d%m%Y %H%M%S'))
with open(name, 'w') as brb:
    brb.write(str(time_taken))
