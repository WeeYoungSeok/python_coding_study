import sys

input = sys.stdin.readline

array = []

n = int(input())

for _ in range(n):
    x = int(input())
    array.append(x)
array.sort()
for i in array:
    print(i)