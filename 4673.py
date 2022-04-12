num = set(range(1, 10001))
cons_num = set()

for i in range(1, 10001):
    for k in str(i):
        i +=int(k)
    cons_num.add(i)
self_num = num - cons_num
for j in sorted(self_num):
    print(j)
