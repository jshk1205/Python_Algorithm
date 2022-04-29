import sys
from collections import deque
n = int(sys.stdin.readline())
que_list =deque([])
for i in range(n):
    commend = sys.stdin.readline().split()
    if commend[0] == 'push':
        que_list.append(commend[1])
    elif commend[0] == 'pop':
        if len(que_list) != 0:
            print(que_list.popleft())
        else:
            print(-1)
    elif commend[0] == 'size':
        print(len(que_list))
    elif commend[0] == 'empty':
        if len(que_list) == 0:
            print(1)
        else:
            print(0)
    elif commend[0] == 'front':
        if len(que_list) == 0:
            print(-1)
        else:
            print(que_list[0])
    elif commend[0] == 'back':
        if len(que_list) == 0:
            print(-1)
        else:
            print(que_list[-1])