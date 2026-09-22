st = [int(x) for x in input().split()]
d = {}
n = st[0]
t = st[1]
k = [int(y) for y in input().split()]
count = 0
for i in k:
    find = t - i
    count += d.get(find, 0)
    d[i] = d.get(i, 0) + 1
    # print(f'{d.get(find, 0)}, {count}, {find}')
print(count)