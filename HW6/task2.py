# Дан список, вывести отдельно буквы и цифры, пользуясь filter

l = [12,'sadf',5643]
numbers = list(filter(lambda i: type(i) == int, l))
strings = list(filter(lambda i: type(i) == str, l))
print(numbers, strings)