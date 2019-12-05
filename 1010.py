def transform(num, radix):
    count = 0
    len_num = len(num)
    for i in range(len_num):
        count += num_dict[num[i]]*pow(radix, len_num-i-1)
    return count


n1, n2, tag, radix = input().split()
radix = int(radix)
num_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12,
            'd': 13, 'e': 14, 'f': 15, 'g': 16, 'h': 17, 'i': 18, 'j': 19, 'k': 20, 'l': 21, 'm': 22, 'n': 23, 'o': 24,
            'p': 25, 'q': 26, 'r': 27, 's': 28, 't': 29, 'u': 30, 'v': 31, 'w': 32, 'x': 33, 'y': 34, 'z': 35}
if tag == '2':
    t = n1
    n1 = n2
    n2 = t
n1_d = transform(n1, radix)
min_range = max(n2)
if not n2.isdigit():
    # print("not")
    min_range = ord(min_range)-86
else:
    min_range = int(min_range)
    if min_range < 2:
        min_range = 2

# print(min_range)
radix2 = 0
for i in range(min_range, 100):
    if n1_d == transform(n2, i):
        radix2 = i
        break
if radix2 == 0:
    print("Impossible")
else:
    print(radix2)

# python
