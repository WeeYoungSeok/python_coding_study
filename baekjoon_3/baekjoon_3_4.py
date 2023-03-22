import sys

x = int(input())

for i in range(x):
    one, two = map(int,sys.stdin.readline().split())
    print(one + two)