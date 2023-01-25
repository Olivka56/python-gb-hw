# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

number = float(input('Enter number: '))
digits = filter(lambda i: i != '-' and i != '.', str(number))
digits_sum = sum(map(int, digits))
print(digits_sum)