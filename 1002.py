dic = {}
for i in range(2):
    x = input().split()
    for j in range(1, len(x)):
        if j % 2 == 1:
            try:
                dic[int(x[j])] += float(x[j + 1])
            except KeyError:
                dic[int(x[j])] = float(x[j + 1])
dic1 = sorted(dic.items(), key=lambda z: z[0], reverse=True)
list1 = []
for i in range(len(dic)):
    if dic1[i][1] != 0:
        list1.append(str(dic1[i][0]))
        list1.append(str(round(dic1[i][1], 1)))
if len(list1) == 0:
    print("0")
else:
    print(int(len(list1) / 2), end=" ")
    print(" ".join(list1))
# 需要注意：
# 1.系数为0的情况需要过滤
# 2.结果为0时不能带空格
