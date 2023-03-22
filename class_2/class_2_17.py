import sys

input = sys.stdin.readline

n = int(input())

array = []
for _ in range(n):
    x, y = map(int, input().split())
    array.append([y, x])

array.sort()
for i in array:
    print(i[1], i[0])