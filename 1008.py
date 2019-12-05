n, *floors = list(map(int, input().split()))
total_time = 5 * n + 6 * floors[0]
for i in range(n-1):
    if floors[i] < floors[i + 1]:
        total_time += 6 * (floors[i + 1] - floors[i])
    else:
        total_time += 4 * (floors[i] - floors[i + 1])
print(total_time)
