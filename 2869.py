import sys
import math
A, B, V = map(int, sys.stdin.readline().split())
day = math.ceil((V-A)/(A-B)) + 1
print(day)
# 시간 초과 코드
# import sys
# A, B, V = map(int, sys.stdin.readline().split())
# temp, day = 0, 0
# while temp + A <= V:
#     temp = temp + A - B
#     day += 1
# print(day)