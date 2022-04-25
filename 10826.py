n = int(input())
num_list = [0,1]
if n >= 0 and n < 10001:
    for _ in range(2, n+1):
        num_list.append(0)

    for i in range(2, n+1):
        num_list[i] = num_list[i-2] + num_list[i-1]
    print(num_list[n])
