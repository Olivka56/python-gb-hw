# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

list = input('Enter numbers separated by spaces: ').split()
list2 = []

for i in range(len(list)):
    list[i] = int(list[i])

for i in range(round(len(list) / 2)):
    list2.append(list[i] * list[-i - 1])
print(list2)


