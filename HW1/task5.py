# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

from math import sqrt

x1 = float(input('Enter x1: '))
y1 = float(input('Enter y1: '))
x2 = float(input('Enter x2: '))
y2 = float(input('Enter y2: '))

length = float(sqrt(x2 - x1) + (y2 - y1))

print(round(length, 3))
