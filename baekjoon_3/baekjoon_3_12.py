import sys

while True:
    one, two = map(int, sys.stdin.readline().split())
    if one > 0 and two > 0:
        print(one + two)
    else:
        break