# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите натуральное число: '))

dividers = []
temp = n

while temp % 2 == 0:
    dividers.append(2)
    temp /= 2

div = 3
while temp > 1:
    if temp % div == 0:
        dividers.append(div)
        temp /= div
    else:
        div += 2

print(n, '=', ' * '.join(map(str, dividers)))
