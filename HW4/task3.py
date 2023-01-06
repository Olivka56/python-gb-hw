# Задайте последовательность чисел.
# Напишите программу, которая выведет список элементов,
# которые не имели повторов в исходной последовательности.

lst = list(map(int, input('Введите числа через пробел: ').split()))

unique = []

def is_unique(element, lst):
    count = 0
    for i in lst:
        if i == element:
            count += 1
    return count == 1

for el in lst:
    if is_unique(el, lst):
        unique.append(el)

print(unique)
