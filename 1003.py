n, m, c1, c2 = map(int, input().split())
rescue_num = list(map(int, input().split()))  # 索引表示的点的点权[每个城市中救援队的数量]
route = [[0 for x in range(n)] for i in range(n)]  # 创建n*n的二维数组，存放L

# for i in range(n):
#         route[i][i] = 0

for i in range(m):
    x, y, z = map(int, input().split())
    route[x][y] = z
    route[y][x] = z

visted = [0 for x in range(n)]
weight = [float('inf') for x in range(n)]  # weight数组存储从起点到索引表示点的最短路径长度
power = [0 for x in range(n)]  # power数组存储从起点到索引表示点的最大点权
num = [0 for x in range(n)]  # num数组存储从起点到索引表示点有几条最短路径

weight[c1] = 0
power[c1] = rescue_num[c1]
visted[c1] = 1
x = c1
num[c1] = 1
while visted[c2] == 0:
    for i in range(n):
        if route[x][i] != 0 and visted[i] != 1:
            if weight[i] >= weight[x] + route[x][i]:
                if weight[i] == weight[x] + route[x][i]:
                    num[i] = num[i] + num[x]
                    if power[i] < power[x] + rescue_num[i]:
                        power[i] = power[x] + rescue_num[i]
                else:
                    if weight[i] > weight[x] + route[x][i]:
                        power[i] = power[x] + rescue_num[i]
                        num[i] = num[x]
                weight[i] = weight[x] + route[x][i]
    small = sorted([weight[x] for x in range(n) if visted[x] != 1])[0]
    index = [x for x in range(n) if weight[x] == small and visted[x] != 1][0]
    visted[index] = 1
    x = index
print(num[c2], power[c2])

# 使用Dijkstra算法求解最短路径
