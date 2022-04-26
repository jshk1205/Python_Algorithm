import sys
n = int(sys.stdin.readline())
stack_list = []
for i in range(n):
    commend = sys.stdin.readline().split()
    if commend[0] == 'push':
        stack_list.append(commend[1])
    elif commend[0] == 'pop':
        if len(stack_list) == 0:
            print(-1)
        else:
            print(stack_list.pop())
    elif commend[0] == 'size':
        print(len(stack_list))
    elif commend[0] == 'empty':
        if len(stack_list) == 0:
            print(1)
        else:
            print(0)
    elif commend[0] == 'top':
        if len(stack_list) == 0:
            print(-1)
        else:
            print(stack_list[-1])