import sys

x = int(input())

for i in range(1, x + 1):
    one, two = map(int, sys.stdin.readline().split())
    print("Case #{}: {}".format(i, one + two))