import sys
a_con, b_con = map(int, sys.stdin.readline().split())
a_num = set(map(int, sys.stdin.readline().split()))
b_num = set(map(int,sys.stdin.readline().split()))

print(len(a_num ^ b_num))