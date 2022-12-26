# Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.


n = int(input('Введите число: '))
list = []
for i in range(-n, n+1):
    list.append(i)
print(list)

second_list = [2, 2, 3, 1, 8]
product = 1
for index in second_list:
    product *= list[index]
print(product)