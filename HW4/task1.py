# Пользователь вводит число
# Вам необходимо вывести число Пи с той точностью знаков после запятой, сколько указал пользователь(БЕЗ round())

from math import pi

n = int(input('Введите число: '))

print(f'{pi:.{n}f}')