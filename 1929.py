m,n = map(int, input().split())

def Prime(num):
    if num ==1:
        return False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

for i in range(m, n+1):
    if Prime(i):
        print(i)
# 시간초과 코드
# m,n = map(int, input().split())
# decimal_list = []
# for i in range(m, n+1):
#     count =0
#     for k in range(2, i+1):
#         if i % k == 0:
#             count += 1
#     if count == 1:
#         decimal_list.append(i)
# for k in decimal_list:
#     print(k)