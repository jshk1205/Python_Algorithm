import sys
n, k = map(int, sys.stdin.readline().split())
num_list = [i for i in range(1, n+1)]
result = []
index = 0
for i in range(n):
    index += k - 1
    if index >= len(num_list):
        index = index % len(num_list)
    result.append(str(num_list.pop(index)))
print('<',', '.join(result)[:],'>',sep='')