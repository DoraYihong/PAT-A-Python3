dic1 = {}
dic2 = {}
dic = {}
x = input().split()
for j in range(1, len(x)):
    if j % 2 == 1:
        dic1[int(x[j])] = float(x[j + 1])
x = input().split()
for j in range(1, len(x)):
    if j % 2 == 1:
        dic2[int(x[j])] = float(x[j + 1])
dic1_keys = list(dic1.keys())
dic2_keys = list(dic2.keys())
for i in dic1_keys:
    for j in dic2_keys:
        try:
            dic[i+j] += dic1[i]*dic2[j]
        except KeyError:
            dic[i + j] = dic1[i] * dic2[j]
sorted_dic = sorted(dic.items(), key=lambda z: z[0], reverse=True)
list1 = []
for i in range(len(dic)):
    if sorted_dic[i][1] != 0:
        list1.append(str(sorted_dic[i][0]))
        list1.append(str(round(sorted_dic[i][1], 1)))
if len(list1) == 0:
    print("0")
else:
    print(int(len(list1) / 2), end=" ")
    print(" ".join(list1))
# 需要注意：
# 1.系数为0的情况需要过滤
# 2.结果为0时不能带空格
