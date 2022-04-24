n, m = map(int, input().split())
card_list = list(map(int, input().split()))
card_list = card_list[:n]
temp = 0
for i in range(n):
    for k in range(i +1, len(card_list)):
        for j in range(k +1, len(card_list)):
            if card_list[i] + card_list[k] + card_list[j] > temp and card_list[i] + card_list[k] + card_list[j] <= m:
                temp = card_list[i] + card_list[k] + card_list[j]
print(temp)