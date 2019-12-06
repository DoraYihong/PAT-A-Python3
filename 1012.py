def rank(num, nums):
    array = list(nums)
    return 1 + array.index(num)
    # return 1


def output(s_id):
    pos = sid.index(s_id)
    temp = analyse[pos]
    pos = temp.index(min(temp))
    print(min(temp), acme[pos])
    # print('1')


n, m = list(map(int, input().split()))
acme = ['A', 'C', 'M', 'E']
sid, score_c, score_m, score_e, score_a = [], [], [], [], []
analyse, input_sid = [], []
for i in range(n):
    x = input().split()
    sid.append(x[0])
    score_c.append(int(x[1]))
    score_m.append(int(x[2]))
    score_e.append(int(x[3]))
    score_a.append((int(x[1]) + int(x[2]) + int(x[3])) / 3)

for i in range(n):
    analyse.append(
        [rank(score_a[i], score_a), rank(score_c[i], score_c), rank(score_m[i], score_m), rank(score_e[i], score_e)])

for i in range(m):
    input_sid.append(input())

for i in range(m):
    if input_sid[i] in sid:
        output(input_sid[i])
    else:
        print("N/A")
