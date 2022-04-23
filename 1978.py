n = int(input())
num_list = list(map(int, input().split()))
num_list = num_list[:n]
decimal_cnt = 0
for i in num_list:
    count =0
    for k in range(1, i+1):
        if i % k == 0:
            count += 1
    if count == 2:
        decimal_cnt += 1

print(decimal_cnt)

