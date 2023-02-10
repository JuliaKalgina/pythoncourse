number = int(input('Type in a number'))
total = 0
while number > 0:
    num2 = number % 10
    total = total + num2
    number = number // 10
print(total)
