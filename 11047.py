n, k = map(int, input().split())
coin_list = []
count_list = []
cSum = 0
for _ in range(0, n):
    coin_list.append(int(input()))
for i in range(len(coin_list)-1,-1, -1):
    if coin_list[i] <= k:
        cSum += k // coin_list[i]
        k = k % coin_list[i]
    if k == 0:
        break
print(cSum)