import sys
import heapq as hpq
n = int(sys.stdin.readline())
num_list =[]
for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if num_list:
            print(hpq.heappop(num_list)[1])
        else:
            print(0)
    else:
        hpq.heappush(num_list, (abs(x),x))