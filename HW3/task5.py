# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def fibonacci(n):
    f = []
    a, b = 1, 1
    for i in range(n):
        f.append(a)
        a, b = b, a + b

    a, b = 0, 1
    for i in range(n + 1):
        f.insert(0, a)
        a, b = b, a - b
    return f

n = int(input('Enter number: '))
print(fibonacci(n))