num = int(input())
result = 1
for i in range(1, num +1):
    result *= i
result = list(str(result))
count = 0
for k in range(len(result)-1, -1 , -1):
    if result[k] == '0':
        count += 1
    else:
        break
print(count)