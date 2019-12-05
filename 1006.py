m = int(input())
id_num = []
sign_in_time = []
sign_out_time = []
for i in range(m):
    x, y, z = input().split()
    id_num.append(x)
    sign_in_time.append(y)
    sign_out_time.append(z)
print(id_num[sign_in_time.index(min(sign_in_time))],id_num[sign_out_time.index(max(sign_out_time))])
