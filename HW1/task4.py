# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input('Enter quarter: '))
if quarter > 4 or quarter < 1:
    print('Enter number from 1 to 4')
else:
    if quarter == 1:
        print('x > 0 and y > 0')
    elif quarter == 2:
        print('x < 0 and y > 0')
    elif quarter == 3:
        print('x < 0 and y < 0')
    else:
        print('x > 0 and y < 0')