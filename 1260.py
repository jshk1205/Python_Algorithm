from collections import deque # 양방향 큐 (양방향 이여서 스택과 큐 형태로 모두 사용 가능)
import sys
read = sys.stdin.readline
n, m, v = map(int, read().split()) # n -> 정점 개수, m -> 간선 개수, v -> 시작 위치

graph = [[0] * (n + 1) for _ in range(n + 1)]
visit_list = [0] * (n + 1)
visit_list2 = [0] * (n + 1)

for _ in range(m):
  a, b = map(int, read().split())
  graph[a][b] = graph[b][a] = 1

def BFS(v):
  q = deque()
  q.append(v)
  visit_list[v] = 1
  while q:
    v = q.popleft()
    print(v, end = ' ')
    for i in range(1, n + 1):
      if visit_list[i] == 0 and graph[v][i] == 1:
        q.append(i)
        visit_list[i] = 1

def DFS(v):
  visit_list2[v] = 1
  print(v, end = ' ')
  for i in range(1, n + 1):
    if visit_list2[i] == 0 and graph[v][i] == 1:
      DFS(i)

DFS(v)
print()
BFS(v)