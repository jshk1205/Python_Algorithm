A = int(input())
B = int(input())
C = int(input())
temp = str(A * B * C)
count = [0 for i in range(10)]
temp_list = list(map(int,temp))
for i in temp_list:
    count[i] += 1
for k in range(len(count)):
    print(count[k])