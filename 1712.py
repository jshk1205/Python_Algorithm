a,b,c = map(int,input().split(' '))
count = 0
total = 0
if b >= c:
    print(-1)
else:
    total = int(a / (c-b))
    print(total + 1)
