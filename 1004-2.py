def dfs(node, depth):
    is_visited[node] = True
    global max_depth
    max_depth = max(max_depth, depth)
    if node not in tree:
        num_leaf_node[depth] += 1
        return
    for child in tree[node]:
        if is_visited[child] is False:
            dfs(child, depth + 1)  # 递归


n, m = list(map(int, input().split(" ")))  # n:树中节点数,m:非叶节点数
tree = {}  # 用字典表示树
max_depth = 0  # 树的深度
num_leaf_node = [0] * (n + 1)  # 同一深度的叶子节点数
is_visited = [False] * (n + 1)  # 节点是否已访问
for i in range(m):  # 初始化树
    node_id, k, *child_id = list(map(int, input().split(" ")))
    tree[node_id] = child_id
dfs(1, 0)
print(" ".join(str(i) for i in num_leaf_node[0:max_depth + 1]))
