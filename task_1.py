def season(mm):
    if month == 12 or month == 1 or month == 2:
        return 'It is Winter'
    elif month == 3 or month == 4 or month == 5:
        return 'It is Spring'
    elif month == 6 or month == 7 or month == 8:
        return 'It is Summer'
    elif month == 9 or month == 10 or month == 11:
        return 'It is Autumn'
    else:
        return 'This month does not exist'


month = int(input('Type in a month number'))
yyy = season(month)
print(yyy)
