n = int(input())
m = int(input())
decimal_list = []
for i in range(n, m+1):
    count =0
    for k in range(1, i+1):
        if i % k == 0:
            count += 1
    if count == 2:
        decimal_list.append(i)
if len(decimal_list) > 0:
    print(sum(decimal_list))
    print(min(decimal_list))
else:
    print(-1)