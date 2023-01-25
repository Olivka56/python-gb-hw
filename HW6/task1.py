# Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа

numbers = map(int, input('Enter numbers: ').split())
two_digits = filter(lambda num: 10 <= num <= 99, numbers)
for num in two_digits:
    print(num, end=' ')