t = int(input())
result = []
for i in range(t):
    result = list(input())
    score, temp = 0, 0
    for k in range(len(result)):
        if result[k] =='O':
            score += temp + 1
            temp += 1
        else:
            temp = 0
    print(score)
