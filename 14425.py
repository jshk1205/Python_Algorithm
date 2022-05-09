import sys
n, m = map(int, sys.stdin.readline().split())
n_list = []
m_list = []
count = 0
for _ in range(n):
    n_list.append(sys.stdin.readline())
for _ in range(m):
    m_list.append(sys.stdin.readline())

for k in range(m):
    if m_list[k] in n_list:
        count += 1
print(count)