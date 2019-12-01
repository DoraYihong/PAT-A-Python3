n, m, c1, c2 = map(int, input().split())
rescue_num = list(map(int, input().split()))  # 索引表示的点的点权[每个城市中救援队的数量]
route = [[float('inf') for x in range(n)] for i in range(n)]  # 创建n*n的二维数组，存放L[点权，城市之间的距离]

for i in range(m):
    x, y, z = map(int, input().split())
    route[x][y] = z
#     route[y][x] = z

is_visited = [False for x in range(n)]
min_length = [float("inf") for x in range(n)]  # 创建距离表，存放最短路径长度，float("inf")表示无穷大
max_rescue_num = [0 for x in range(n)]  # 最大救援队的数量
num = [0 for x in range(n)]  # 最短路径数量

min_length[c1] = 0
max_rescue_num[c1] = rescue_num[c1]
is_visited[c1] = True
x = c1
num[c1] = 1
while is_visited[c2] is False:
    for i in range(n):  # 遍历起点x，找到起点x的邻接顶点
        if route[x][i] != float('inf') and is_visited[i] is False:  # 遍历起点x，找到起点x的邻接顶点
            # 先到x，再从x到i的距离，与已有的直接到i的距离进行比较
            if min_length[i] >= min_length[x] + route[x][i]:  # 如果距离表中x的距离+x到i的距离<=距离表中i的距离
                if min_length[i] == min_length[x] + route[x][i]:  # 距离相等的情况
                    num[i] = num[i] + num[x]  # 更新最短路径数量，但最大救援队数量不一定需要更新
                    if max_rescue_num[i] < max_rescue_num[x] + rescue_num[i]:  # 已知最大救援队数量小于实际最大救援队数量的情况
                        max_rescue_num[i] = max_rescue_num[x] + rescue_num[i]  # 更新最大救援队数量
                else:  # 距离不相等，也就是距离表中x的距离+x到i的距离<距离表中i的距离的情况
                    if min_length[i] > min_length[x] + route[x][i]:  # 距离表中x的距离+x到i的距离<距离表中i的距离的情况
                        max_rescue_num[i] = max_rescue_num[x] + rescue_num[i]  # 更新最大救援队数量
                        num[i] = num[x]  # 更新最短路径数量
                min_length[i] = min_length[x] + route[x][i]  # 更新距离表
    small = sorted([min_length[x] for x in range(n) if is_visited[x] is False])[0]  # 从距离表中找到出发距离最短的点
    index = [x for x in range(n) if min_length[x] == small and is_visited[x] is False][0]  # 找到该距离最短的点的编号
    is_visited[index] = True  # 标记该点已访问，避免重复访问
    x = index  # 更新x点，进入下一轮循环

print(num[c2], max_rescue_num[c2])

# 使用Dijkstra算法求解最短路径
