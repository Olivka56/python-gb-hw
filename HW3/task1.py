# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

list = input('Enter numbers separated by spaces: ').split()
for i in range(len(list)):
    list[i] = int(list[i])
s = 0
for i in range(1, len(list), 2):
    s += list[i]
print(f'The sum of the elements of the list is: {s}')