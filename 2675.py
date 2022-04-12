for i in range(int(input())):
    round, text = input().split()
    text = list(text)
    result =[]
    for j in range(len(text)):
        for k in range(int(round)):
            result.append(text[j])
    print(''.join(result))