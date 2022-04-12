c = int(input())
for i in range(c):
    count = 0
    ngrade = list(map(int, input().split()))
    n = ngrade.pop(0)
    ave = sum(ngrade) / n
    for k in range(len(ngrade)):
        if ngrade[k] > ave:
            count += 1
    print("{:.3f}".format((count/n)*100) + '%')
