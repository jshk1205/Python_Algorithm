for i in range(int(input())):
    k = int(input())
    n = int(input())
    total = [p for p in range(1,n+1)]
    for __ in range(k):
        for j in range(1, n):
            total[j] += total[j - 1]
    print(total[-1])