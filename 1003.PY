if __name__ == "__main__":
    line = input().split(" ")
    n = int(line[0])
    m = int(line[1])
    c1 = int(line[2])
    c2 = int(line[3])
    line = input().split(" ")
    point = [int(x) for x in line]
    route = [[0 for x in range(n)] for i in range(n)]
    for x in range(m):
        line = input().split(" ")
        a = int(line[0])
        b = int(line[1])
        c = int(line[2])
        route[a][b] = c
        route[b][a] = c
    visted = [0 for x in range(n)]
    weight = [float('inf') for x in range(n)]
    power = [0 for x in range(n)]
    weight[c1] = 0
    power[c1] = point[c1]
    visted[c1] = 1
    x = c1
    num = [0 for x in range(n)]
    num[c1] = 1
    while visted[c2] == 0:
        for i in range(n):
            if route[x][i] != 0 and visted[i] != 1:
                if weight[i] >= weight[x] + route[x][i]:
                    if weight[i] == weight[x] + route[x][i]:
                        num[i] = num[i] + num[x]
                        if power[i] < power[x] + point[i]:
                            power[i] = power[x] + point[i]
                    else:
                        if weight[i] > weight[x] + route[x][i]:
                            power[i] = power[x] + point[i]
                            num[i] = num[x]
                    weight[i] = weight[x] + route[x][i]
        small = sorted([weight[x] for x in range(n) if visted[x] != 1])[0]
        index = [x for x in range(n) if weight[x] == small and visted[x] != 1][0]
        visted[index] = 1
        x = index

    print(num[c2], power[c2])
