n = int(input())
round, num, size = 1, 1, 6 #round -> 지나가야 하는 방의 수, size -> 커지는 크기
while num < n:
    round += 1
    num += size
    size += 6
print(round)


