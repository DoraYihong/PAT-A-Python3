k = int(input())
array = list(map(int, input().split()))
if max(array) < 0:
    print("0", array[0], array[k - 1])
else:
    max_count = array[0]
    begin = end = 0
    for i in range(k):
        count = 0
        for j in range(i, k):
            count += array[j]
            if count > max_count:
                max_count = count
                begin = i
                end = j
    print(max_count, array[begin], array[end])
# 暴力求解，测试点7超时
