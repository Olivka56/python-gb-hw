# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

number = int(input('Enter a day of week number: '))

if number > 7 or number < 1:
    print('Enter number from 1 to 7')
elif number < 6:
    print('NO')
else:
    print('YES')

