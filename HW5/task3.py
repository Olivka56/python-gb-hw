# RLE алгоритм

import rle

with open('data.txt', 'rt') as f:
    data = f.readline()

r = rle.compress(data)
print(r)

r = rle.decompress(r)
print(r)
