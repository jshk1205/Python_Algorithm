import sys
import heapq as hpq
n = int(sys.stdin.readline())
num_list =[]
for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(num_list) == 0:
            print(0)
        else:
            print(hpq.heappop(num_list))
    else:
        hpq.heappush(num_list, x)