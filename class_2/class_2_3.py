import sys

input = sys.stdin.readline

n = int(input())

array = []
for _ in range(n):
    inner = list(map(int, input().split()))
    array.append(inner)

array.sort()
for i in array:
    print(i[0], i[1])