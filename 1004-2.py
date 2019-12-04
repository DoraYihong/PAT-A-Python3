def dfs(node, depth):
    global max_depth
    max_depth = max(max_depth, depth)
    print(node, depth)
    is_visited[node] = 1
    if tree.get(node, -1) == -1:  # 没有子节点
        level[depth] += 1
        return
    for child in tree[node]:  # dfs遍历当前节点的所有子节点
        if is_visited[child] == 0:
            dfs(child, depth + 1)  # 递归


# n:树中节点数
# m:非叶节点数
n, m = list(map(int, input().split(" ")))
if n == 1:  # 只有一个节点直接输出1
    print("1")
else:
    tree = {}  # 树
    max_depth = 0
    level = [0] * (n+1)  #
    is_visited = [0] * (n+1)  # 是否已访问
    # 初始化树
    for i in range(m):
        # x = input().split(" ", 2)
        # node_id = x[0]
        # child_id = x[2].split()
        # print(child_id)
        node_id, k, *child_id = list(map(int, input().split(" ")))
        tree[node_id] = child_id
    dfs(1, 0)  # 从根节点开始遍历
    # print("child_id:", child_id)
    print("tree:", tree)
    print("level:", level)
    print("max_depth:", max_depth)
    print("is_visited", is_visited)
    print(" ".join(str(i) for i in level[0:max_depth+1]))
