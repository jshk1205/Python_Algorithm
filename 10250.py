for i in range(int(input())):
    H, W, N = map(int, input().split()) # H -> 층수, W -> 방 수, N -> 손님 순서
    hight = int(N % H)
    if hight == 0:
        hight = H
        width = N // H
    else :
        width = N // H + 1
    if width < 10 :
        width = '0'+ str(width)
    print(hight, width, sep='')
