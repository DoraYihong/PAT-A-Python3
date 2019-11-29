a, b = map(int, input().split())
c = a+b
d = abs(c)
sign = '' if c >= 0 else '-'
if d < 1000:
    print(c)
else:
    e = str(d)
    print(sign, end="")
    for i in range(len(e)):
        print(e[i], end="")
        if (len(e)-i) % 3 == 1 and i != len(e)-1:
            print(',', end="")
