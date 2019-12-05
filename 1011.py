wtl = ['W', 'T', 'L']
output = []
profit = 1
for i in range(3):
    x = list(map(float, input().split()))
    output.append(wtl[x.index(max(x))])
    profit *= max(x)
output.append(str(round((profit * 0.65 - 1) * 2, 2)))
print(" ".join(output))
