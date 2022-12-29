# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

bn = ""
dn = int(input('Enter number: '))

while dn != 0:
    bn = str(dn % 2) + bn
    dn //= 2

print(bn)
