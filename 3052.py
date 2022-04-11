num = [int(input()) for i in range(10)]
count = []
for i in range(len(num)):
    temp = num[i] %42
    count.append(temp)
count = set(count)
print(len(count))