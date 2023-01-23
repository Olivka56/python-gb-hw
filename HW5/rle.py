def compress(data):
    start = data[0]
    count = 0
    result = ''
    for char in data:
        if char.isdigit():
            raise ValueError('string cannot include digits')
        if char == start:
            count += 1
        else:
            result += f'{count}{start}'
            count = 1
            start = char
    result += f'{count}{start}'
    return result

def decompress(data):
    number = 0
    result = ''
    for char in data:
        if char.isdigit():
            number = number * 10 + int(char)
        else:
            result += char * number
            number = 0
    return result
