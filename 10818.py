n = int(input())
num = list(map(int, input().split()))
num = num[:n]
print(num)
print(min(num),max(num))