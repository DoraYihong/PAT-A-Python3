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
min_range = max([int(x, 36) for x in n2]) + 1
# 对分查找
left = max(int(x, 36) for x in n2) + 1
right = max(left, n1_d)
radix2 = 0
while left <= right:
    middle = round((left + right) / 2)
    t = transform(n2, middle)
    if t == n1_d:
        radix2 = middle
        break
    else:
        if t > n1_d:
            right = middle - 1
        else:
            left = middle + 1
if radix2 == 0:
    print("Impossible")
else:
    print(radix2)
