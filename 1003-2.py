n, m, c1, c2 = map(int, input().split())
rescue_num = list(map(int, input().split()))  # 每个城市中救援队的数量
distance = [[float('inf') for i in range(n)] for j in range(n)]  # 城市之间的距离
for i in range(m):
    x, y, z = map(int, input().split())
    distance[x][y] = z


min_distance_num = [0 for i in range(n)]  # 最短路径数量
max_rescue_num = [0 for i in range(n)]  # 最大救援队数量
max_rescue_num[c1] = rescue_num[c1]

# 使用Dijkstra算法求解最短路径
distance_table = [float('inf') for i in range(n)]  # 距离表
distance_table[c1] = 0
is_traversed = [False for i in range(n)]  # 是否已遍历
is_traversed[c1] = True
x = c1  # 设定遍历起点
min_distance_num[c1] = 1
while is_traversed[c2] is False:  # 直到c2被遍历，结束循环
    for i in range(n):  # 遍历x的邻接顶点
        if is_traversed[i] is False and distance[x][i] != float("inf"):  # 顶点可达且邻接顶点未被遍历的情况
            # 将已知直接到i的距离与先到x，再从x到i的距离进行比较
            if distance_table[i] > distance_table[x] + distance[x][i]:  # 如果先到x，再从x到i的距离更近
                min_distance_num[i] = min_distance_num[x]  # 更新最短路径数量
                max_rescue_num[i] = max_rescue_num[x] + rescue_num[i]  # 更新最大救援队数量
                distance_table[i] = distance_table[x] + distance[x][i]  # 更新距离表
            elif distance_table[i] == distance_table[x] + distance[x][i]:  # 如果先到x，再从x到i的距离与已知直接到i的距离相同
                min_distance_num[i] = min_distance_num[i] + min_distance_num[x]  # 更新最短路径数量
                if max_rescue_num[i] < max_rescue_num[x] + rescue_num[i]:  # 如果最大救援队数量小于实际最大救援队数量
                    max_rescue_num[i] = max_rescue_num[x] + rescue_num[i]  # 更新最大救援队数量
    is_traversed[x] = True
    next_data = sorted([distance_table[j] for j in range(n) if is_traversed[j] is False])[0]  # 从距离表中找到出发距离最短的点
    next_index = [j for j in range(n) if distance_table[j] == next_data and is_traversed[j] is False][0]
    x = next_index

print(min_distance_num[c2], max_rescue_num[c2])
