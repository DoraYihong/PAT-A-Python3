num = int(input())
line = input().split(" ")
number = [int(x) for x in line]
flag = True
if len([x for x in number if x >= 0]) == 0:
    flag = False
    print(0, number[0], number[-1])
sums = -1
temp, tempLeft, index, right, left = 0, 0, 0, 0, 0
if flag is True:
    while index != len(number):
        temp = temp + number[index]
        index += 1
        if temp < 0:
            temp = 0
            tempLeft = index
        elif temp > sums:
            sums = temp
            left = tempLeft
            right = index - 1
    print(sums, number[left], number[right])
